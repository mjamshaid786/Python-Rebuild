
import csv
#-------------1. READING CSV DATA FUNCTION ----------------
sales_data = []
def read_sales_data():
    try:
        with open('09 CSV Sales Analyzer/sales.csv', 'r') as sales:
            reader = csv.DictReader(sales)
            sales_data = list(reader)
            return sales_data
    except FileNotFoundError:
        print("Check file path and existance of file please and also name of the file!")

#-------------2. ORDER'S TOTAL FUNCTION ---------------- Calculate total values for each item
def calculate_order_total(sales_data):
    total_quantity = {}
    item_price = {}
    for item in sales_data:
        product = item['product']
        quantity = int(item['quantity'])
        price = int(item['price'])
        if product in total_quantity:
            total_quantity[product] += quantity
        else:
            total_quantity[product] = quantity
        product = item['product']
        quantity = int(item['quantity'])
        if product in item_price:
            item_price[product] = price
        else:
            item_price[product] = price
    return total_quantity, item_price

#-------------3. TOTAL SALES FUNCTION ----------------
def total_sale(total_sales, prices):
    prices_list = 0
    for product, total in total_sales.items():
        prices_list += prices[product] * total
    return prices_list

#-------------4.BEST SALING PRODUCT FUNCTION ----------------
def best_selling_product(total_sales):
    highest_product_sold = max(total_sales, key=total_sales.get)
    return highest_product_sold, total_sales[highest_product_sold]

#-------------5. SALES BUY CATEGORY FUNCTION ----------------
def category_sales(sales_data):
    categories = {}
    for category in sales_data:
        cat = category['category']
        price = int(category['price'])
        quantity = int(category['quantity'])

        if cat in categories:
            categories[cat] += (price * quantity) 
        else:
            categories[cat] = price * quantity
    return categories



def total_quantity(total_sales):
    over_all_orders = 0
    for t in total_sales.values():
        over_all_orders += t
    return over_all_orders

#========================================
#                MAIN
#========================================


sales_data = read_sales_data()
# for p in sales_data:
#     # print(f"{p['product']} price = {p['price']}")
total_sales, prices = calculate_order_total(sales_data)
# for product, total in total_sales.items():
#     # print(f"{product} -->  {prices[product]} x {total} = {prices[product] * total}")

total = total_sale(total_sales, prices)
# print(total)
product, max_sold = best_selling_product(total_sales)
# print(f"{product} : {max_sold}")

category_vise_sales = category_sales(sales_data)


#======================================
#           FINAL OUTPUT
#======================================
print("=" * 30)
print("         SALES ANALYSIS         ")
print(f'{"=" * 30}\n')
t_orders = total_quantity(total_sales)
print(f"Total Orders        : {len(sales_data)}")

print(f"Total Sales         : Rs. {total}")
print(f"Total Quantity Sold : {t_orders}\n")
print(f"Average Order Value: Rs. {total / (len(sales_data))}")
print("- " * 15)
print(" Sales by Category              ")
print(f'{"- " * 15}\n')
for cat, sum in category_vise_sales.items():
    print(f"{cat}           : Rs. {sum}")
print("- " * 15)
print(" Best Selling Product              ")
print(f'{"- " * 15}\n')

print(f"Product             : {product}")
print(f"Quantity Sold       : {max_sold}")
print("=" * 30)