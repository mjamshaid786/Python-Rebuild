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