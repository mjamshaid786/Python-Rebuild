# Task 7 — Username Creator Ask the user for their first name and last name. Create a username by taking the first 3 letters of the first name and the first 3 letters of the last name, joined together in lowercase. Print the username.

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

user_name = first_name[0:3].lower() + last_name[0:3].lower()
print(user_name)