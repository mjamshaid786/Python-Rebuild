import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")


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
            for user in final_users:
                    payload = {"id": user.get('id', 'N/A'),
                        "full_name": user.get('fullName', 'N/A'),
                        "email": user['email', 'N/A'],
                        "age": user['age', 'N/A'],
                        "city": user['city', 'N/A'],
                        "company" : user['company', 'N/A']
                        }
            

            # Convert data into bytes and send to kafka
                    bytes_data = json.dumps(payload).encode('utf-8')
                    producer.produce(topic_name, value=bytes_data)
                    producer.flush()
            logger.info("Data Produced Successfully.")
        elif user_choice == "0":
            break
    except ValueError:
                print("Please Enter Valid Option !")
                continue
print("Producer Closed.")
