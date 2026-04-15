FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Instalar pydantic primero con versiones exactas para evitar conflictos
RUN pip install --no-cache-dir \
    pydantic==2.11.9 \
    pydantic-core==2.33.2 \
    pydantic-settings==2.10.1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]