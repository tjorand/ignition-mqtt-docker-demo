FROM python:3.12-slim
WORKDIR /app
COPY client.py .
RUN pip install --no-cache-dir paho-mqtt
CMD ["python", "client.py"]