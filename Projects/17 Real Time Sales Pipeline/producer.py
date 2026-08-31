import json
from confluent_kafka import Producer

# 1. Kafka Connection Setup

try:
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    # 2. Topic Name
    topic_name = 'sales'

    print("Producer Ready! Type Message and Press Enter ('exit' to stop):")

    while True:
        try:
            user_choice = input(f"Enter 1 to Add Item OR Enter 0 to Exit : ").strip()
            if user_choice == "1":
                while True:
                    try:
                        order_id = int(input("Enter Order ID: "))
                        if order_id >= 0:
                            break
                        print("Add positive values only!")
                    except ValueError:
                        print("Order ID contains only integers (101, 112, etc)")
                
                while True:
                    product_name = input("Enter Product Name: ").strip().title()
                    if not product_name:
                        print("Product name can not be empty!")
                        continue       
                    if not product_name.replace(" ", "").isalpha():
                        print("Product name can not contain numbers or special character!")
                        continue
                    break

                while True:
                    try:
                        price = int(input("Enter Price: "))
                        if price >= 0:
                            break
                        print("Add positive values only!")
                    except ValueError:
                        print("Price contains only integers (101, 112, etc)")
                
                while True:
                    try:
                        quantity = int(input("Enter Quantity: "))
                        if quantity >= 0:
                            break
                        print("Add positive values only!")
                    except ValueError:
                        print("Quantity contains only integers (101, 112, etc)")
                total = price * quantity
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
except Exception as e:
    print("ERROR: ", e)
