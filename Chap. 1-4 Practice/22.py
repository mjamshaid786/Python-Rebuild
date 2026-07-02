# Task 22 — Password Strength Checker Ask the user to enter a password. Print the result of a single boolean expression using and that checks all of these at once: the length is 8 or more, it contains the symbol "@", and it does not contain a space.

password = input("Enter password: ")
print( len(password) >= 8 and "@" in password and " " not in password)