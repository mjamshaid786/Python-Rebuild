import json
from confluent_kafka import Consumer
from psycopg2.extras import execute_values
from table import conn
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
        msg = consumer.poll(1.0)  
        if msg is None:
            continue
        if msg.error():
            print("There is an Error", msg.error())
            continue


        data = json.loads(msg.value().decode('utf-8'))
        
        print(f"""\nReceived\n 
                Order ID    : {data['order_id']}
                Price       : {data['price']}
                Product Name: {data['product']}
                Quantity    : {data['quantity']}
                Total       : {data['total']} """)
        with conn.cursor() as cur:
            values = [
                (data['order_id'], data['product'], data['price'], data['quantity'], data['total'])
            ]
            query = """
            --sql
            INSERT INTO sales (order_id, product, price, quantity, total) VALUES %s ON CONFLICT (order_id) DO NOTHING
            ;
            """
            execute_values(cur, query, values)
            conn.commit()
            print("Saved to PostgreSQL")

except KeyboardInterrupt:
    print("\nConsumer Closed.")
finally:
    consumer.close()
