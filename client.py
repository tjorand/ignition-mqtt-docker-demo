import paho.mqtt.client as mqtt
import time

# MQTT broker details
BROKER = "host.docker.internal"  # If broker runs on your host machine
PORT = 1883
TOPIC = "test/topic"

# Callback when connection is established
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received: {msg.topic} -> {msg.payload.decode()}")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Start loop in background
client.loop_start()

# Example publishing every 5 seconds
try:
    while True:
        message = "Hello from Docker MQTT client!"
        client.publish(TOPIC, message)
        print(f"Published: {message}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()