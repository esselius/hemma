import paho.mqtt.client as mqtt
from pydantic import ValidationError

from events import Event


def on_connect(client: mqtt.Client, userdata, flags, rc):
    client.subscribe("deconz")


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    try:
        event = Event.validate_json(msg.payload)
        print(event.__repr__())
    except ValidationError as err:
        print(msg.payload)
        print(err)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost")

client.loop_forever()
