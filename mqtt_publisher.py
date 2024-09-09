import paho.mqtt.client as mqtt
import time

# Define the broker address and port
broker_address = "localhost"  # or "127.0.0.1"
broker_port = 1883

# Create a new MQTT client instance
client = mqtt.Client("PublisherClient")

# Connect to the broker
client.connect(broker_address, broker_port)

# Define the topic to publish to
topic = "test/topic"

# Publish messages 
counter = 1
try:
    while True:
        message = "Hello MQTT, message number {}".format(counter)
        client.publish(topic, message)
        print("Message '{}' sent to topic '{}'".format(message, topic))
        counter += 1
        time.sleep(1)  # Delay for 1 second between messages
except KeyboardInterrupt:
    print("Stopping publisher...")

# Disconnect from the broker
client.disconnect()
