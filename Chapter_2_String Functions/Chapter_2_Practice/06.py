# 6.Password Masker: User se ek password input lein. Pehle aur aakhri character ko chhor kar beech ke tamam characters ko * se replace kar dein (e.g., secret ban jaye s****t).

password = input("Enter password: ")
#print(password[1:-1])
#print(len(password[1:-1]))
middle_pass = "*" * len(password[1:-1])
print(f"{password[0]}{middle_pass}{password[-1]}")