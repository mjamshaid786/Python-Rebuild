# ===================================
#       2. ADD PRODUCT FUNCTION
# ===================================
inventory = []
def add_product():
    #______________ PRODUCT ID _______________
    while True:
        try:
            product_id = int(input("Enter Product ID: "))
            if product_id >= 0:
                break
            print("Add positive values only!")
        except ValueError:
            print("Product ID contains only integers (101, 112, etc)")
    #______________ PRODUCT NAME _______________
    while True:
        product_name = input("Enter Product Name: ").strip().title()
        if not product_name:
            print("Product name can not be empty!")
            continue       
        if not product_name.replace(" ", "").isalpha():
            print("Product name can not contain numbers or special character!")
            continue
        break
    #______________ PRODUCT CATEGORY _______________
    while True:
        product_category = input("Enter Product Category: ").strip().title()
        if not product_category:
            print("Product category can not be empty!")
            continue       
        if not product_category.replace(" ", "").isalpha():
            print("Product category can not contain numbers or special character!")
            continue
        break
    #______________ PRODUCT PRICE _______________
    while True:
        try:
            product_price = int(input("Enter Product Price: "))
            if not product_price:
                print("Product price can not be empty!")
                continue       
            if product_price > 0:
                break
            print("Product price can not contain negative numbers")
            continue
        except ValueError:
            print("Product price can not contains alphabets or special character")
    #______________ PRODUCT QUANTITY _______________
    while True:
        try:
            product_quantity = int(input("Enter Product Quantity: "))
            if not product_quantity:
                print("Product quantity can not be empty!")
                continue       
            if product_quantity >= 0:                
                break
            print("Product quantity can not contain negative numbers!")
            continue
        except ValueError:
            print("Product quantity can not contains alphabets or special character")
    inventory.append({'id' : product_id, 'name' : product_name, 'category' : product_category, 'price' : product_price, 'quantity' : product_quantity})
    print("Product addedd successfully!")



# ===================================
#      2. DISPLAY PRODUCTS FUNCTION
# ===================================

def display_products(inventory):
    if not inventory:
        print("Inventory is empty! Add some products first.")
        return
    print("\n=========================================")
    print("               INVENTORY                 ")
    print("=========================================")
    print(f"{'ID' :<5} {'Product' :<8} {'Category' :<8} {'Price' : <8} {'Quantity' : <8}")       

    for item in inventory:
        print(f"{item['id']:<5} {item['name']:<8} {item['category']:<8} {item['price']:<8} {item['quantity']:<8}")

#========================================
#         3. SEARCH PRODUCT FUNCTION
#========================================
def search_product(inventory):
    while True:
        try:
            search_id = int(input("Enter Product ID: "))
            if search_id >= 0:
                for product in inventory:
                    if product['id'] == search_id:
                        print("Product Found:")
                        print(f"Name: {product['name']}\nCategory: {product['category']}\nPrice: {product['price']}\nQuantity: {product['quantity']}")
                        break
                else:
                    print(f"Product Not Found")
                break
            else:
                print("Add positive values only!")                
        except ValueError:
            print("Product ID contains only integers (101, 112, etc)")

#========================================
#        4. UPDATE QUANTITY FUNCTION
#========================================
def update_quantity(inventory):
    while True:
        try:
            search_id = int(input("Enter Product ID: "))
            if search_id >= 0:
                for product in inventory:
                    if product['id'] == search_id:
                        print("Product Found:")
                        print(f"Name: {product['name']}\nCategory: {product['category']}\nPrice: {product['price']}\nQuantity: {product['quantity']}")
                        update = int(input("Enter new quantity: "))
                        product['quantity'] = update
                        print("Quantity updated successfully!")
                        break
                else:
                    print(f"Product Not Found")
                break
            else:
                print("Add positive values only!")                
        except ValueError:
            print("Product ID contains only integers (101, 112, etc)")
#========================================
#        5. REMOVE PRODUCT FUNCTION
#========================================
def remove_product(inventory):
    while True:
        try:
            search_id = int(input("Enter Product ID: "))
            if search_id >= 0:
                for index, product in enumerate(inventory):
                    if product['id'] == search_id:
                        removed_item = inventory.pop(index)
                        print(f"{removed_item['name']} is removed from inventory")
                        break
                else:
                    print(f"Product Not Found")
                break
            else:
                print("Add positive values only!")                
        except ValueError:
            print("Product ID contains only integers (101, 112, etc)")
#========================================
#        6. LOW STOCK FUNCTION
#========================================    
def low_stock_products(inventory):
    found = False
    for stock in inventory:
        if stock['quantity'] < 5:
            print(f"{stock['name']} --> {stock['quantity']}")
            found = True
    if not found: # if found is stll False
        print("No low stock products")
#==============================================
#        7. INVENTORY VALUE FUNCTION
#==============================================
def inventory_value(inventory):
    total_value = 0
    for item in inventory:
        value = item['price'] * item['quantity']
        print(f"{item['name']} --> {item['price']} x {item['quantity']} = {item['price'] * item['quantity']}")
        total_value += value
    print("- " * 15)
    print(f"Total Inventory Values = Rs. {total_value}")

#==============================
#         MAIN MENU
#==============================

while True:
    user_input = input('''
    ====================================
        INVENTORY MANAGEMENT SYSTEM
    ====================================
        1. Add Produc
        2. Dispplay Products
        3. Search Product
        4. Update Quanity
        5. Remove Product
        6. Low Stock Products
        7. Inventory Value
        8. Exit
        :''')

    match user_input:
        case "1":
            add_product()
        case "2":
            display_products(inventory)
        case "3":
            search_product(inventory)
        case "4":
            update_quantity(inventory)
        case "5":
            remove_product(inventory)
        case "6":
            low_stock_products(inventory)
        case "7":
            inventory_value(inventory)
        case "8":
            break
        case _:
            print("Invalid choice! Please enter a number between 1 and 8.")



