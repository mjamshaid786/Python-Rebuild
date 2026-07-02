#Task 4 — Smart Home Power Tariff Estimator
#	Scenario: An smart electricity billing system factoring in peak hours and slab rates.
#•	Input: Total units consumed (kWh) and time of usage ("Peak" or "Off-Peak").
#•	Logic:
#o	First 100 units rate: Rs. 15 per unit.
#o	Units consumed beyond 100 rate: Rs. 25 per unit.
#o	If the usage was during "Peak" hours, apply a 15% surcharge on the total bill.
#•	Output: Display Total Units, Basic Cost, Surcharge, and Final Bill amount.


units = int(input("Enter consumed units: "))
time = input("Consumption time was Peak OR Off-Peak: ").lower()

# 1. Calculate basic cost using progressive tiers (slabs)
if units <= 100:
    basic_cost = units * 15
else:
    basic_cost = (100 * 15) + ((units - 100) * 25)

# 2. Calculate surcharge based on timing
surcharge = 0
if time == "peak":
    surcharge = basic_cost * 0.15

# 3. Calculate final payable amount
final_bill = basic_cost + surcharge

# 4. Single clean output window
print("\n" + "="*30)
print("       ELECTRICITY INVOICE      ")
print("="*30)
print(f"Total Units Consumed : {units} kWh")
print(f"Basic Cost           : Rs. {basic_cost:.2f}")
print(f"Peak Surcharge (15%) : Rs. {surcharge:.2f}")
print("-"*30)
print(f"Final Payable Amount : Rs. {final_bill:.2f}")
print("="*30)