# 7.Bill Splitter: Total bill amount aur doston ki tadad input lein. Har dost ke hisse mein kitne paise aate hain, wo calculate karke print karein.

total_bill = int(input("Enter total bill: "))
no_of_frnds = int(input("No. of friends: "))

for_each = total_bill / no_of_frnds
print(for_each)