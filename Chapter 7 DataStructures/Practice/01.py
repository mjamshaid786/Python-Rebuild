total_classes = 80
attendted = int(input("Enter the classes you attended: "))
percentage = (attendted / total_classes) * 100 
print("You attendence is ", percentage, "%")

if percentage < 75:
    print("You are not Eligible !")
    need = 75 - percentage
    print(f"You need {need}% more attendence for Eligibility")
else:
    print("You are Eligible")


