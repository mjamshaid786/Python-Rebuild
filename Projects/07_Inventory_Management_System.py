# ===================================
#       ADD PRODUCT FUNCTION
# ===================================
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
                print("Product addedd successfully!")
                break
            print("Product quantity can not contain negative numbers!")
            continue
        except ValueError:
            print("Product quantity can not contains alphabets or special character")



# ===================================
#      DISPLAY PRODUCTS FUNCTION
# ===================================







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



