# Task 19 — BMI Calculator Ask the user for their weight in kg and height in meters. Calculate BMI using weight / height ** 2 and print the result rounded to 1 decimal place.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / height ** 2
print(round(bmi, 1))