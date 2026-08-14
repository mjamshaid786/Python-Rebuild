# ===================================
#       ADD PRODUCT FUNCTION
# ===================================
def add_product():
    while True:
        try:
            product_id = int(input("Enter Product ID: "))
            if product_id >= 0:
                break
            print("Add positive values only!")
        except ValueError:
            print("Product ID contains only integers (101, 112, etc)")
    
    while True:
        product_name = input("Enter Product Name: ").strip().title()
        if not product_name:
            print("Product name can not be empty!")
            continue       
        if not product_name.replace(" ", "").isalpha():
            print("Product name can not contain numbers or special character!")
            continue
        break





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



