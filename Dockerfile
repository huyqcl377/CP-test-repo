
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    python3-venv \
    curl \
    libpq-dev \
    && apt-get clean

WORKDIR /app/

COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
