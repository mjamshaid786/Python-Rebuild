# Filter Evens: Create a new list containing only the even numbers from an existing list of integers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_number = []

for n in numbers:
    if n %2 == 0:
        even_number.append(n)

print(even_number)
    
