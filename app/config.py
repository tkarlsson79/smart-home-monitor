# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "localhost")
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "home/sensors/#")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./smart_home.db")
