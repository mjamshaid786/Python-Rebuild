#===================================
#       SMART EXPENSE TRACKER
#===================================
expenses = []
while True:
        while True:
            expense_category = input("Enter Category: ").strip().title()
            if expense_category:
                print(f"Category: {expense_category}")
                break
            print("Catgory can not be empty! Try Again.")
        while True:
            try:                
                amount = int(input("Enter amount: "))
                if amount >= 0:
                    break
                else:
                    print("Negative amount is not allowed")
            except ValueError:
                print("Alphabets and Special characters are not allowed!")
        expenses.append({"category" : expense_category, "amount" : amount})
        print(f"{expense_category} : {amount}  is added successfully!")
        new_item = input("Do you want to add new expense: y/n : ").strip().lower()
        if new_item != "y":
             print("Items added Successfully !")
             break

print('''
========================
      TOTAL EXPENSE
========================
''')
total_expense = []
for expense in expenses:
     print(f"{expense['category']}: Rs. {expense['amount']}")

print("- " * 13)
for te in expenses:
     total_expense.append(te['amount'])
# print(total_expense)
print(f"Total Expenses: {sum(total_expense)}")

'''---- HIGHEST AND LOWEST EXPENSE ----'''
category_total = {}
for exp in expenses:
     cat = exp['category']
     amnt = exp['amount']

     if cat in category_total:
          category_total[cat] += amnt
     else:
          category_total[cat] = amnt

for cat, total in category_total.items():
     print(f"{cat}: Rs.{total}")
print("- " * 13)
highest_category = max(category_total, key=category_total.get)
lowest_category = min (category_total, key=(category_total.get))

print(f"Highest Expense: {highest_category} - Rs.{category_total[highest_category]}")
print(f"Lowest Expense: {lowest_category} - Rs.{category_total[lowest_category]}")