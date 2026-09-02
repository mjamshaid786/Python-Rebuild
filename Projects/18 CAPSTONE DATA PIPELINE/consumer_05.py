import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")
import json
from confluent_kafka import Consumer

# 1. Kafka Connection Setup
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-simple-group',
    'auto.offset.reset': 'earliest'
})
# 2. Topic Subscribe 
topic_name = 'sales'
consumer.subscribe([topic_name])

print("Consumer Listening... (Press Ctrl+C to stop)")

# 3. Message Listen Loop
try:
    while True:
        msg = consumer.poll(1.0)  # After every 1 second ask kafka for messsage.

        if msg is None:
            continue
        if msg.error():
            continue

        # Bytes ko String aur fir JSON me decode karein
        data = json.loads(msg.value().decode('utf-8'))
        
        print(f"\nReceived -> Sender: {data['sender']} | Message: {data['message']}")

except KeyboardInterrupt:
    print("\nConsumer Closed.")
finally:
    consumer.close()


