FROM python:3.12-slim-bookworm

RUN apt-get update && \
    apt-get install -y build-essential

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["echo", "Hello 👋"]