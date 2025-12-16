#app/simulated_sensors.py
import json
import math
import random
from datetime import datetime, timezone
import time

import paho.mqtt.client as mqtt
from app.config import MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_TOPIC

SENSORS = [
    {"device_id": "livingroom", "sensor_type": "temperature", "unit": "°C"},
    {"device_id": "bedroom", "sensor_type": "humidity", "unit": "%"},
    #{"device_id": "bedroom", "sensor_type": "light", "unit": "lux"},
]

def main():
    client = mqtt.Client()
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
    try:
        while True:
            for sensor in SENSORS:
                if sensor["sensor_type"] == "temperature":
                    value = 20 + 5 * math.sin(time.time() / 60) + random.uniform(-0.5, 0.5)
                elif sensor["sensor_type"] == "humidity":
                    value = 40 + 10 * math.sin(time.time() / 90) + random.uniform(-1, 1)
                elif sensor["sensor_type"] == "light":
                    value = max(0, 300 * math.sin(time.time() / 120) + random.uniform(-10, 10))
                else:
                    value = 0

                payload = {
                    "device_id": sensor["device_id"],
                    "sensor_type": sensor["sensor_type"],
                    "value": round(value, 2),
                    "unit": sensor["unit"],
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
                client.publish(MQTT_TOPIC.replace("#", f"{sensor['device_id']}/{sensor['sensor_type']}"), json.dumps(payload))
                print(f"Published: {payload}")

            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping simulated sensors...")
    finally:
        client.loop_stop()

if __name__ == "__main__":
    main()