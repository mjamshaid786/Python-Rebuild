# ==================================================
#               STUDENT GRADE ANALYZER
# ==================================================
print('''
==================================
      STUDENT GRADE REPORT
==================================
''')
name = input("Enter your name: ").title()
id = input("Enter your ID: ")

# =======================================
#        GETTING USER MARKS
# ========================================
python_marks = int(input("Enter your Python Marks: "))
if python_marks < 0 or python_marks > 100:
    print("Please Enter Valid Marks")

sql_marks = int(input("Enter your SQL Marks: "))
if sql_marks < 0 or python_marks > 100:
    print("Please Enter Valid Marks")

database_marks = int(input("Enter your Database Marks: "))
if database_marks < 0 or python_marks > 100:
    print("Please Enter Valid Marks")

networking_marks = int(input("Enter your Networking Marks: "))
if networking_marks < 0 or python_marks > 100:
    print("Please Enter Valid Marks")

mathematics_marks = int(input("Enter your Mathematics Marks: "))
if mathematics_marks < 0 or python_marks > 100:
    print("Please Enter Valid Marks")