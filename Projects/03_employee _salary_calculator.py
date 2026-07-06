'''----------EMPLOYEE SALARY CALCULATOR----------'''
'''-----Check Name Validaton-----'''
def emp_name (name: str) -> bool:
    cleaned_name = name.strip().replace(" ", "")
    return bool(cleaned_name.isalpha())

'''----------BASIC SALARY & OVER TIME----------'''
def gross_salary (salary: int):
    try:
        if salary > 0:
            basic_salary = salary
            over_time_hours = int(input("Enter over_time hours: "))
            over_time_rate = 10
            over_time_salary = over_time_hours * over_time_rate
            print(f"Your over time salary is: {over_time_salary}")
            return basic_salary + over_time_salary
        else:
            print("Enter a positive interger value (e.g, 500, 2500) !")
    except:
        print("Enter valid salary amount !")        

'''----------MAIN----------'''
name = input("Enter your name: ")
if emp_name(name):
    print(f"Welcome Mr. {name.title()}")
else:
    print("Please enter a valid name !")

salary = int(input("Enter your basic salary: "))
total_salary = gross_salary(salary)
print("-" * 10, "SALARY SLIP", "-" * 10)
print(f"Your total salary is: {total_salary}")