import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker com código {rc}")
    client.subscribe("test/topic", qos=0)

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1884, 60)
client.loop_forever()