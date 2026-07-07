burger = 550
pizza = 1200
drink = 180
b = 0
p = 0
d = 0
name = input("What is your good name: ")

while True:
    b += burger *  int(input("How many Burgers you want: "))
    print("Bill is :", b)
    p += pizza * int(input("How many pizzaz you want: "))
    print("Bill is :", b + p)
    d += drink * int(input("How many drinks you want: "))
    print("Bill is :", b + p + d)
    user = input("Press b to show bill :").lower()
    total  = b + p + d
    if user == "b":
        break
    else:
        print("Please Reorder !")
if total > 3000:
    discount = total * 0.10
    total -= discount
    print(f"Your total Bill is : {total}")
else:
    print(f"Your total Bill is : {total}")
