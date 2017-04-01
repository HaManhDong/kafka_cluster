from kafka.client import KafkaClient
from kafka import KafkaConsumer


#client = KafkaClient(boostrap_servers='localhost:9092');



consumer = KafkaConsumer('topic1',
                          bootstrap_servers=['localhost:9092'])
print consumer.topics()
print consumer.subscription()

for message in consumer:
    print("%s:%d:%d: key=%s value=$s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
