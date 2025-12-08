# app/api.py
from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from .database import get_db
from . import models, schemas

router = APIRouter()


@router.get("/readings", response_model=List[schemas.SensorReadingRead])
def get_readings(
    sensor_type: Optional[str] = None,
    device_id: Optional[str] = None,
    minutes: int = 60,
    db: Session = Depends(get_db),
):
    """
    Hämta senaste readings, default sista 60 minuterna.
    """
    since = datetime.utcnow() - timedelta(minutes=minutes)
    query = db.query(models.SensorReading).filter(models.SensorReading.timestamp >= since)

    if sensor_type:
        query = query.filter(models.SensorReading.sensor_type == sensor_type)
    if device_id:
        query = query.filter(models.SensorReading.device_id == device_id)

    return query.order_by(models.SensorReading.timestamp.asc()).all()
