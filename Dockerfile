FROM python:3.12-slim

WORKDIR /app

# System-deps (ta bort om du inte behöver bygga native-grejer)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Installera Poetry
RUN pip install --no-cache-dir poetry

# Kopiera in metadata + README (behövs pga readme-fältet i pyproject)
COPY pyproject.toml poetry.lock* README.md ./

# Installera dependencies, men inte projektet som paket
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi --no-root

# Kopiera in resten av koden
COPY . .

# Starta med hot reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
