import pulsar
client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')
producer.send(b'Hello Pulsar!')
client.close()