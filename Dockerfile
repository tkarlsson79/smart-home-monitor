FROM python:3.12-slim

# Configure Poetry
ENV POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

# Optional system deps (bra att ha för ev. builds)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir "poetry==${POETRY_VERSION}"

# Copy only pyproject (och ev. lock) först
COPY pyproject.toml /app/
# COPY poetry.lock /app/   # om du vill använda lock-filen

# Install dependencies i *global* env i containern (ingen venv)
RUN poetry install --no-root --no-ansi

# Copy resten av koden (app, main.py, static, README, osv.)
COPY . /app

# Exponera FastAPI-porten
EXPOSE 8000

# Starta appen
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
