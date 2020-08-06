import paho.mqtt.client as mqtt
import datetime
HOSTNAME = "mqtt.eclipse.org"

def on_connect(client, userdata, flags, rc):

    client.subscribe("mqttsimulator/#")

def on_message(client, userdata, msg):
    print(str(datetime.datetime.now())+" - "+msg.topic+" -  "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.username_pw_set("USUARIO", password="SENHA")

client.connect(HOSTNAME, 1883, 60)

client.loop_forever()