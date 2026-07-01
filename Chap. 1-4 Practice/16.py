# Task 16 — Celsius to Fahrenheit Ask the user for a temperature in Celsius. Convert it using F = (C * 9/5) + 32 and print the result rounded to 2 decimal places.

temp_in_celcius = float(input("Enter temperature in Celsius: "))
Farenheat = (temp_in_celcius * 9/5) + 32
print(f"Temperature in Farenheat: {round(Farenheat, 2)}")