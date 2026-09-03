import logging
import logger_config
logger = logging.getLogger(f"project_18_logger.{__name__}")
import json
from confluent_kafka import Consumer
from psycopg2.extras import execute_values
from database_06 import conn
# 1. Kafka Connection Setup
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-simple-group',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
})

# 2. Topic Subscribe 
topic_name = 'users'
consumer.subscribe([topic_name])

print("Consumer Listening... (Press Ctrl+C to stop)")

# 3. Message Listen Loop
try:
    while True:
        msg = consumer.poll(1.0)  
        if msg is None:
            continue
        if msg.error():
            print("There is an Error", msg.error())
            continue

        try:
            data = json.loads(msg.value().decode('utf-8'))
            logger.info("Data Received.")
            print(f"""\nReceived\n 
                    User ID    : {data['id']}
                    Name       : {data['full_name']}
                    Email      : {data['email']}
                    Age        : {data['age']}
                    City       : {data['city']}
                    Company    : {data['company']} """)
            with conn.cursor() as cur:
                values = [
                    (data.get('id'), data.get('full_name'), data.get('email'), data.get('age'), data.get('city'), data.get('company'))
                ]
                query = """
                --sql
                INSERT INTO users (id, full_name, email, age, city, company) VALUES %s ON CONFLICT (id) DO NOTHING
                ;
                """
                execute_values(cur, query, values)
                conn.commit()
                consumer.commit(message=msg, asynchronous=False)
                logger.info("Inserting Data Into Database")
                logger.info("Saved to PostgreSQL")
        except json.JSONDecodeError as e:
            logger.error(f"Failed To Decode JSON Payload, {e}")
        except Exception as db_err:
            conn.rollback()
            logger.error(f"Database Insertion Error: {db_err}")

except KeyboardInterrupt:
    print("\nConsumer Closed.")
finally:
    consumer.close()
    if conn:
        conn.close()
        logger.info("Database connection closed.")
