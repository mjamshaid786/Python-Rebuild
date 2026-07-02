# Task 21 — Username Validator Ask the user to enter a username. Using and, print the result of a single boolean expression that checks: the length is greater than 4, it does not contain a space, and it is not equal to "admin".

username = input("Enter username: ")

print(len(username) > 4 and " " not in username and username != "admin")