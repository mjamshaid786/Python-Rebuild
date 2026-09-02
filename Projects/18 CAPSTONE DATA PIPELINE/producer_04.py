import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")
from flattening_users_data_03 import data_flattening, users
users = data_flattening(users)
import json
from confluent_kafka import Producer # for installng Run --> pip install confluent-kafka (verify using [pip list | Select-String "confluent-kafka"]

# 1. Kafka Connection Setup
try:
    logger.info("Connecting To Producer...")
    producer = Producer({'bootstrap.servers': 'localhost:9092'})
except:
    logger.error("Failed To Connect Producer !")
# 2. Topic Name
topic_name = 'users'
logger.info("Topic Created --> ", topic_name)

logger.info("Producer Is Ready To Send Data.")

while True:
        try:
            user_choice = input(f"Enter 1 to Add Item OR Enter 0 to Exit : ").strip()
            if user_choice == "1":
                ok
            elif user_choice == "0":
                break
            
            else:
                print("Please Enter Valid Value")
                continue
        except ValueError:
            print("Please Enter Valid Option !")
            continue

        # Message Payload
        payload = {"order_id": order_id,
                    "product": product_name,
                    "price": price,
                    "quantity": quantity,
                    "total": total
                    }
        

        # Convert data into bytes and send to kafka
        bytes_data = json.dumps(payload).encode('utf-8')
        producer.produce(topic_name, value=bytes_data)
        producer.flush()

print("Producer Closed.")
