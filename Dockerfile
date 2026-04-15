FROM python:3.11-slim

WORKDIR /app

# Dependencias críticas del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt .
# Forzamos que ignore conflictos menores para avanzar
RUN pip install --no-cache-dir -r requirements.txt --use-deprecated=legacy-resolver || \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]