#Task 1 — E-Commerce Dynamic Shipping & Discount Engine
#•	Scenario: Build a billing logic system for an online store.
#•	Input: Total purchase amount (float) and customer type ("Regular" or "VIP").
#•	Logic:
#	If the purchase amount is greater than Rs. 5000, apply a 10% discount.
#	If the customer is "VIP", apply an additional 5% discount on top of the already #discounted price.
#	Shipping Charges: If the final price (after discounts) is less than Rs. 3000, add a Rs. #250 shipping fee. Otherwise, shipping is free.
#	Output: Print the Original Price, Discount Amount, Shipping Fee, and Final Payable Amount.


purchase_amount = int(input("Enter purchase amount: "))
customer_type = input("Are you VIP or Regular customer:").lower()

if purchase_amount >= 5000:
    discount = purchase_amount * (10 / 100)
    if customer_type == "vip":
        vip_discount = purchase_amount * (5 /100)
        final_discount = discount + vip_discount
        print(f"Original Price: {purchase_amount}\nDicount Amount: {final_discount}\nShipping Fee: \nFinal Payable Amount: {purchase_amount - final_discount}")
    else:
        print(f"Original Price: {purchase_amount}\nDicount Amount: {discount}\nShipping Fee: \nFinal Payable Amount: {purchase_amount - discount}")
elif purchase_amount <= 3000:
    Shipping_fee= 250
    print(f"Original Price: {purchase_amount}\nDicount Amount: 0\nShipping Fee: {Shipping_fee}\nFinal Payable Amount: {purchase_amount + Shipping_fee}")
else:
    print(f"Original Price: {purchase_amount}\nDicount Amount: 0\nShipping Fee: 0\nFinal Payable Amount: {purchase_amount}")