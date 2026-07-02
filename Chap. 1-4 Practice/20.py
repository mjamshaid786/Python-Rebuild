# Task 20 — Discount Calculator Ask the user for an original price and a discount percentage. Calculate the amount saved using price * discount / 100 and the final price. Print both rounded to 2 decimal places.

price = int(input("Enter Original Price: "))
discount = int(input("Enter discount in %: "))
save_amount = price * discount / 100

final_price = price - save_amount
print(f"Your final price is: {round(final_price, 2)}\nYou saved: Rs.{round(save_amount, 2)}")