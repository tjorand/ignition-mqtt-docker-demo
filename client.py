import os
import time
import paho.mqtt.client as mqtt

BROKER = os.getenv("BROKER_HOST", "mqtt-broker")
PORT = 1883
TOPIC = "test/topic"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to {BROKER} with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Received: {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        message = "Hello from Docker MQTT client!"
        client.publish(TOPIC, message)
        print(f"Published: {message}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()