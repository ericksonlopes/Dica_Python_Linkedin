import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1884, 60)

for i in range(5):
    mensagem = f"Olá MQTT #{i+1}"
    client.publish("test/topic", mensagem, qos=0)
    print(f"Publicada: {mensagem}")
    time.sleep(2)

client.disconnect()