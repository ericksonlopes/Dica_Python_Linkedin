import pulsar
client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic', subscription_name='my-sub')
msg = consumer.receive()
print(msg.data())
consumer.acknowledge(msg)
client.close()