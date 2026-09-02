import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")
import json
from confluent_kafka import Consumer