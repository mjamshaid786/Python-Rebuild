#Task 2 — ATM Cash Denomination Optimizer
#•	Scenario: An ATM machine needs to dispense cash using the largest #bills possible.
#•	Input: Withdrawal amount from the user (must be a multiple of 500, e.#g., 1500, 4500).
#	Logic: Validate the input first. If the amount is not a multiple of #500, print an error. If valid, calculate the minimum number of Rs. 5000, #Rs. 1000, and Rs. 500 notes required to fulfill the amount.
#•	Output: Print the breakdown of the notes (e.g., "5000 notes: 2, 1000 notes: 1, 500 notes: 0").


amount = int(input("Enter amount (Must be multiple of 500, eg 1500, 4500): "))

if amount % 500 == 0:
    # 1. Get 5000 notes and find the remaining balance
    five_thousand = amount // 5000
    amount %= 5000  # This updates 'amount' to whatever is left over
    
    # 2. Get 1000 notes from the remaining balance
    one_thousand = amount // 1000
    amount %= 1000  # Updates 'amount' again
    
    # 3. Get 500 notes from whatever is left
    five_hundred = amount // 500
    
    # Output the results
    print(f"5000 notes: {five_thousand}")
    print(f"1000 notes: {one_thousand}")
    print(f"500 notes: {five_hundred}")
else:
    print("Invalid Input! Please enter an amount that is a multiple of 500.")