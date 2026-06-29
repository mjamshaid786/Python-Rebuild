# Generate a random integer between 1-100 and check if it is even or odd.
import random
number = random.randint(1,100)
print(number)

print(number % 2 == 0)
print("Even")
print(number % 2 != 0)
print("Odd")