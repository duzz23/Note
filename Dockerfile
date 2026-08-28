FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN mkdir -p /app/data

CMD ["python", "main.py"]
