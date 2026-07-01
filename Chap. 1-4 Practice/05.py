# Task 5 — Simple Receipt Ask the user for a product name and its price. Print a receipt line like: Item: Apple | Price: $3.99

item = input("Enter product name: ")
price = float(input("Enter price: "))

print(f"Item: {item} | Price ${price}")