import paho.mqtt.client as mqtt

# Define the broker address and port
broker_address = "localhost"
broker_port = 1883

# Callback function when a message is received
def on_message(client, userdata, message):
    print("Message received: {} on topic {}".format(message.payload.decode('utf-8'), message.topic))

# Create a new MQTT client instance
client = mqtt.Client("SubscriberClient")

# Connect to the broker
client.connect(broker_address, broker_port)

# Assign the on_message callback function
client.on_message = on_message

# Subscribe to the topic
topic = "test/topic"
client.subscribe(topic)

# Start the client loop to continuously check for messages
client.loop_start()

print("Subscribed to topic '{}'".format(topic))

# Keep the script running to listen for messages
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()
