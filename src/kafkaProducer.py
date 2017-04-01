from kafka import KafkaProducer
from kafka.errors import KafkaError
import log

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

future = producer.send('topic1', b'raw_bytes')

try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)