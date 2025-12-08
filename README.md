# Smart Home Monitor

Smart Home Monitor is a lightweight Python-based system for collecting, storing, and visualizing home sensor data in real time.  
It uses FastAPI as the backend API, SQLite for storage, MQTT for ingesting sensor messages, and a minimal web dashboard for displaying charts.

---

## Features

- Receives sensor data via MQTT (e.g., temperature, humidity)
- Stores time-stamped data in a SQLite database
- Provides REST API endpoints for querying data
- Includes a simple web dashboard built with Chart.js
- Easy to extend with additional sensors or data types
- Suitable for Raspberry Pi, local servers, or home lab environments

---
## Flow
MQTT Sensor → MQTT Broker → Python MQTT Client → SQLite Database → FastAPI API → Web Dashboard


## Roadmap

- Add alert rules (temperature threshold, humidity alerts, etc.)
- Add notifications (email, Discord, Telegram)
- Add WebSocket real-time updates instead of polling
- Add authentication and user management
- Add support for additional sensor types (CO₂, PM2.5, VOC, power usage)
- Optional Docker deployment setup

---
## License
This project is licensed under the MIT License.

---
## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/smart-home-monitor.git
cd smart-home-monitor
python install poetry
poetry install
```

### 2 Configure
.env
MQTT_BROKER_HOST=localhost
MQTT_BROKER_PORT=1883
MQTT_TOPIC=home/sensors/#
DATABASE_URL=sqlite:///./smart_home.db
