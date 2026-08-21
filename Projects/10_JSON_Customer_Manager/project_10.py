import json
try:
    with open ("10_JSON_Customer_Manager/customer.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("File Note Found")
    


#---------------- 1. Display Customer Function ---------------- 
def display_customer(data):
    print("===========================")
    print("        CUSTOMERS          ")
    print("===========================")
    for customer in data:
        print(f"ID : {customer['id']}\nName : {customer['name']}\nCity : {customer['city']}\n")


#---------------- 2. Search Customer Function ----------------
def search_customer(data):
    while True:
        try:
            id = int(input("Enter Customer ID: "))
            if id > 0:
                for customer in data:
                    if id == customer['id']:
                        print("Customer Found")
                        print(f"Name: {customer['name']}")
                        print(f"City: {customer['city']}")
                        break
                else:
                    print("Customer Not Found!")
                break
            else:
                print("Enter positives values greater than 0 !")
        except ValueError:
            print("ID contains only numbers!")
    

#---------------- 3. Customer Order Function ----------------
def show_customer_order(data):
    while True:
        try:
            id = int(input("Enter Customer ID: "))
            if id > 0:
                for customer in data:
                    if id == customer['id']:
                        print("Customer Found")
                        print(f"Customer: {customer['name']}\n")
                        print(f"Orders: ")
                        for order in customer['orders']:
                            print(f"{order['product']}--> Rs. {order['amount']}")
                        break
                else:
                    print("Customer Not Found!")
                break
            else:
                print("Enter positives values greater than 0 !")
        except ValueError:
            print("ID contains only numbers!")

#---------------- 4. Customer Spendings Function ----------------
def customer_spendings(data):
    for customers in data:
        total = 0
        for orders in customers['orders']:
            total += orders['amount']
        print(f"{customers['name']} Total Spendings Rs. {total}")
        
#---------------- 5. Add New Customer Function ----------------
def add_new_customer(data):
    #------------- ID ---------------
    while True:
        new_customer = {}
        try:
            id = int(input("Enter Customer ID: "))
            if id > 0:
                 for customer in data:
                     if id == customer['id']:
                         print("Customer already exists !")
                         break
                 else:
                    print("Valid ID.")
                    break
            else:
                print("Enter positives values greater than 0 !")
        except ValueError:
            print("ID contains only numbers!")

    #------------- NAME ---------------
    while True:
        try:
            name = input("Enter Customer Name: ").strip().title()
            if not name:
                 print("Name can not be empty")
                 continue
            elif not name.replace(" ", "").isalpha():
                print("Name can not contain numbers or special characters")
                continue
            break
        except ValueError:
            print("Name can not contain numbers or special character")
            continue
    #------------- CITY ---------------
    while True:
        try:
            city = input("Enter City Name: ").strip().title()
            if not city:
                 print("City name can not be empty")
                 continue
            elif not city.replace(" ", "").isalpha():
                print("City name can not contain numbers or special characters")
                continue
            break
        except ValueError:
            print("City name can not contain numbers or special characters")
            continue
    new_customer['id'] = id
    new_customer['name'] = name
    new_customer['city'] = city
    new_customer['orders'] = []
    print("Customer added Successfully ! ")
    return new_customer

#---------------- 6. Add Order To Existing  Customer Function ----------------
def add_order(data):
    while True:
        try:
            id = int(input("Enter Customer ID: "))
            if id > 0:
                 for customer in data:
                     if id == customer['id']:
                         while True:
                            try:
                                item = input("Enter Product Name: ").strip().title()
                                if not item:
                                    print("Name can not be empty")
                                    continue
                                elif not item.replace(" ", "").isalpha():
                                    print("Name can not contain numbers or special characters")
                                    continue
                                order = {}
                                order['product'] = item
                                while True:
                                    try:
                                        price = int(input("Enter amount: "))
                                        if not price > 0:
                                            print("Price Can not be zero or Negative")
                                            continue
                                        order['amount'] = price
                                        customer['orders'].append(order)
                                        print("Order Added Successfully !")
                                        return data
                                    except ValueError:
                                        print("Price can not contain alphabets or Special characters !")
                            except ValueError:
                                print("Name can not contain numbers or special character")
                                continue
                         
                     
                         
                 else:
                    "Customer ID Not Found !"
                    break
            else:
                print("Enter positives values greater than 0 !")
        except ValueError:
            print("ID contains only numbers!")
    
#---------------- 7. Save New Data Function ----------------
def save_data(data):
    with open("10_JSON_Customer_Manager/new_customers_data.json", "w") as file:
        json.dump(data, file, indent=2)
    print("Data Saved Successfully !")






# =========================================
#               MAIN MENU
# =========================================
while True:
    user_input = input('''
        1. Display customer
        2. Search Customers
        3. Show Customer Orders
        4. Show Customer Spendings
        5. Add New Customer
        6. Add Order
        7. Save Data
        8. Exit               




    ---> : ''')




    match user_input:
        case "1":
            display_customer(data)
        case "2":
            search_customer(data)
        case "3":
            show_customer_order(data)
        case "4":
            customer_spendings(data)
        case "5":
            new = add_new_customer(data)
            data.append(new)
        case "6":
            add_order(data)
        case "7":
            save_data(data)
        case "8":
            break
        case _:
            print("Invalid choice! Please enter a number between 1 and 7.")