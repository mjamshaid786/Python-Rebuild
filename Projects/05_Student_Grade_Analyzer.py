# ==================================================
#               STUDENT GRADE ANALYZER
# ==================================================

name = input("Enter your name: ").title()
id = input("Enter your ID: ")

# =======================================
#        GETTING USER MARKS
# ========================================
python_marks = int(input("Enter your Python Marks: "))
if python_marks < 0 or python_marks > 100:
    print("Please Enter Valid Marks")
