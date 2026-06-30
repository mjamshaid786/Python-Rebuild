# Task 2 — Full Name Builder Ask the user for their first name and last name separately. Join them together with a space and print the full name in title case.

first_name = input("Enter first name: ").title()
second_name = input("Enter second name:  ").title()
full_name = first_name + " " + second_name
print(full_name)
