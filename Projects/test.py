expenses = []  # Added items store karne ke liye list

while True:
    print("\n--- Add New Expense ---")
    
    # 1. Category Input Validation (Ensuring it's not empty)
    while True:
        expense_category = input("Enter Category: ").strip().title()
        if expense_category:
            break
        print("Category khali nahi ho sakti! Dobara enter karein.")
    
    # 2. Amount Input Validation
    while True:
        try:
            amount = int(input("Enter amount: "))
            if amount >= 0:
                break
            else:
                print("Negative amount allowed nahi hai!")
        except ValueError:
            print("Alphabets aur special characters allowed nahi hain!")

    # Expense success message & storing
    expenses.append({"category": expense_category, "amount": amount})
    print(f"✅ {expense_category} expense (Rs. {amount}) successfully add ho gaya hai!")

    # 3. Next Item Confirmation Loop
    again = input("\nKya aap koi aur expense add karna chahte hain? (y/n): ").strip().lower()
    if again != 'y':
        print("\nPipeline execution completed!")
        break

# Added items summary
print("\n--- Total Added Expenses ---")
for exp in expenses:
    print(f"- {exp['category']}: Rs. {exp['amount']}")