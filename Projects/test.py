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
        
