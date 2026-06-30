# User se unka first name aur last name alag alag input lein. Output is format mein show karein: "Hello, LASTNAME, Firstname!" (Last name poora uppercase mein aur first name ka pehla letter capital ho).

first_name = input("Enter you first name: ").capitalize()
last_name = input("Enter you last name: ").upper()

print(f"Hello, {last_name}, {first_name}")