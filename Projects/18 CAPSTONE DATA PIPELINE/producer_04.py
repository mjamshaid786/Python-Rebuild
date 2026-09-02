import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")

import json
from confluent_kafka import Producer # for installng Run --> pip install confluent-kafka (verify using [pip list | Select-String "confluent-kafka"]

# 1. Kafka Connection Setup
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# 2. Topic Name
topic_name = 'sales'

print("Producer Ready! Message type karein aur Enter dabayein ('exit' to stop):")

while True:
    msg = input("> ")
    
    if msg == 'exit':
        break

    # Message Payload
    payload = {"sender": "Muhammad Jamshaid", "message": msg}

    # Data ko Bytes me convert karke Kafka ko bhejna
    bytes_data = json.dumps(payload).encode('utf-8')
    producer.produce(topic_name, value=bytes_data)
    producer.flush()

print("Producer Closed.")