# app/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base


class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    sensor_type = Column(String, index=True)  # e.g. temperature, humidity
    value = Column(Float)
    unit = Column(String)  # e.g. "°C", "%"
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
