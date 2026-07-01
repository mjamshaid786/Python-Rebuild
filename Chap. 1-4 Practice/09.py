# Task 9 — Area & Perimeter Ask the user for the length and width of a rectangle. Calculate and print the area (length * width) and the perimeter (2 * (length + width)).

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

area = length * width
perimeter = 2 * ( width + length )

print(f"Area of Rectangle: {area}\nPerimeter of Rectangle: {perimeter}")