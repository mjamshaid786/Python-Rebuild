# Task 18 — Initials Extractor Ask the user for their first, middle, and last name separately. Extract the first character from each using index [0], convert to uppercase, and print them separated by dots. Example: J.K.R

first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
last_name = input("Enter last name: ")

print(f"{first_name[0].capitalize()}.{second_name[0].capitalize()}.{last_name[0].capitalize()}")