# app/mqtt_client.py
import json
import threading
import paho.mqtt.client as mqtt
from .config import MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_TOPIC
from .database import SessionLocal
from .models import SensorReading


def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected to MQTT broker with result code", rc)
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print("MQTT message on", msg.topic, ":", payload)

    try:
        data = json.loads(payload)
        device_id = data.get("device_id", "unknown")
        sensor_type = data.get("sensor_type", "unknown")
        value = float(data.get("value"))
        unit = data.get("unit", "")

        db = SessionLocal()
        reading = SensorReading(
            device_id=device_id,
            sensor_type=sensor_type,
            value=value,
            unit=unit,
        )
        db.add(reading)
        db.commit()
        db.refresh(reading)
        db.close()
    except Exception as e:
        print("Error processing MQTT message:", e)


def start_mqtt_client():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

    thread = threading.Thread(target=client.loop_forever, daemon=True)
    thread.start()
    return client
