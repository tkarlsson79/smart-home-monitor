# app/schemas.py
from datetime import datetime
from pydantic import BaseModel


class SensorReadingBase(BaseModel):
    device_id: str
    sensor_type: str
    value: float
    unit: str


class SensorReadingCreate(SensorReadingBase):
    pass


class SensorReadingRead(SensorReadingBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
