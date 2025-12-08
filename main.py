# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.database import Base, engine
from app import api
from app.mqtt_client import start_mqtt_client

# Skapa DB-tabeller
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Home Monitor")

# Mounta statiska filer
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def startup_event():
    # starta MQTT-klienten i bakgrunden
    start_mqtt_client()


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


# API-router
app.include_router(api.router, prefix="/api", tags=["readings"])
