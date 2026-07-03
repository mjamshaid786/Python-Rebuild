#Task 5 — Daily Expense Accumulator
#	Scenario: A simple personal finance tool to calculate total spendings.
#	Task: Write a for loop that runs exactly 7 times (for 7 days). Each time, ask the user for that day's expense and print the running total at the end.


total_expense = 0

for e in range (1, 8):
    expense = int(input("Enter Today's expense: "))
    total_expense += expense
    print(f"Your total expense is {total_expense}")
