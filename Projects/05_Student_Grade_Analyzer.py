# ==================================================
#               STUDENT GRADE ANALYZER
# ==================================================

name = input("Enter your name: ").title()
id = input("Enter your ID: ")


#=======================================
#        GETTING USER MARKS
#=======================================
while True:
    try:
        python_marks = int(input("Enter your Python Marks: "))
        if 0 <= python_marks <= 100:
            print(f"Your marks are added: {python_marks}")
            break
        else:
            print("Please Enter Valid Marks")
    except ValueError:
        print("Please Enter Valid Marks")
        
while True:
    try:
        sql_marks = int(input("Enter your SQL Marks: "))
        if 0 <= sql_marks <= 100:
            print(f"Your marks are added: {sql_marks}")
            break
        else:
            print("Please Enter Valid Marks")
    except ValueError:
        print("Please Enter Valid Marks")
while True:
    try:
        database_marks = int(input("Enter your Database Marks: "))
        if 0 <= database_marks <= 100:
            print(f"Your marks are added: {database_marks}")
            break
        else:
            print("Please Enter Valid Marks")
    except ValueError:
        print("Please Enter Valid Marks")
while True:
    try:
        networking_marks = int(input("Enter your Networking Marks: "))
        if 0 <= networking_marks <= 100:
            print(f"Your marks are added: {networking_marks}")
            break
        else:
            print("Please Enter Valid Marks")
    except ValueError:
        print("Please Enter Valid Marks")
while True:
    try:
        mathematics_marks = int(input("Enter your Mathematics Marks: "))
        if 0 <= mathematics_marks <= 100:
            print(f"Your marks are added: {mathematics_marks}")
            break
        else:
            print("Please Enter Valid Marks")
    except ValueError:
        print("Please Enter Valid Marks")

#===============================
#       CALCULATIONS
#===============================
obtained_marks = (python_marks + sql_marks + database_marks + networking_marks + mathematics_marks)
total_marks = 500
percentage = (obtained_marks / total_marks) * 100
average = obtained_marks / 5

if 90 <= percentage <=100:
    grade = "A+"
elif 80 <= percentage <=89:
    grade = "A"
elif 70 <= percentage <=79:
    grade = "B"
elif 60 <= percentage <=69:
    grade = "C"
elif 50 <= percentage <=59:
    grade = "D"
else:
    grade = "F"

if percentage >= 50:
    status = "PASS"
else:
    status = "FAIL"




#====================================
#           FINAL OUTPUT
#====================================
print('''
==================================
      STUDENT GRADE REPORT
==================================
''')
print(f"Student Name : {name}")
print(f"Student ID   : {id}\n")
print("-"*34)
print(f"Python       : {python_marks}")
print(f"SQL          : {sql_marks}")
print(f"Database     : {database_marks}")
print(f"Networking   : {networking_marks}")
print(f"Mathematics  : {mathematics_marks}\n")
print(f"{"- " * 18}\n")

print(f"Total        : {obtained_marks} / {total_marks}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Average      : {average}")
print(f"Grade        : {grade}")
print(f"Status       : {status}")