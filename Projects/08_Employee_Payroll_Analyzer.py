#=================================
#       PAYROLL ANALYZER
#=================================
payroll = []
def get_user_info():
    #--------------- 1. ID ---------------
    while True:
        try:
            employee_id = int(input("Enter Employee ID: "))
            if employee_id > 0:
                break                
            else:
                print("Negatives numbers are not allowed!")
        except ValueError:
            print("ID only contains numbers!")
    #--------------- 2. NAME ---------------
    while True:
        try:
            name = input("Enter Employee Name: ").strip().title()
            if not name:
                print("Name can not be empty!")
                continue
            if not name.replace(" ", "").isalpha():
                print("Name can not contain numbers or special characters!")
                continue
            break
        except TypeError:
            print("Name can not include numbers or special characters!")
    #--------------- 3. SALARY ---------------
    while True:
        try:
            salary = int(input("Enter Basic Salary: "))
            if salary > 0:
                break
            else:
                print("Salary can not be zero or negative numbers !")
                continue
        except ValueError:
            print("Salary can only contain numeric values !")
    #--------------- 4. ALLOWANCE ---------------
    while True:
        try:
            allowance = int(input("Enter Allowance: "))
            if allowance > 0:
                break
            else:
                print("Allowance can not be zero or negative numbers !")
                continue
        except ValueError:
            print("Allowance can only contain numeric values !")
    #--------------- 5. TAX ---------------
    while True:
        try:
            tax = int(input("Enter Tax: "))
            if tax > 0:
                break
            else:
                print("Tax can not be zero or negative numbers !")
                continue
        except ValueError:
            print("Tax can only contain numeric values !")

    payroll.append({'id' : employee_id, 'name': name, 'salary' : salary, 'allowance' : allowance, 'tax' : tax })

#========================================
#       GROSS SALARY FUNCTION
#========================================
def gross_salary(payroll):
    for salary in payroll:
        gross_salary = salary['salary'] + salary['allowance']
        return gross_salary

#========================================
#       NET SALARY FUNCTION
#========================================
def net_salary(g_salary, payroll):
    for salary in payroll:
        net_salary = g_salary - salary['tax']
        return net_salary




#========================================
#               MAIN
#========================================
get_user_info()
g_salary = gross_salary(payroll)
n_salary = net_salary(g_salary, payroll)
#========================================
#               REPORT
#========================================
print("=" * 40)
print("         EMPLOYEE PAYROLL        ")
print(F'{"=" * 40}\n')
for id in payroll:
    print(f"Employee ID   : {id['id']}")
for name in payroll:
    print(f"Employee Name : {name['name']}\n")
for salary in payroll:
    print(f"Basic Salary  : Rs. {salary['salary']}")
for allowance in payroll:
    print(f"Allowance     : Rs. {allowance['allowance']}")
print(f"Gross Salary  : Rs. {g_salary}")
for tax in payroll:
    print(f"Tax           : Rs. {tax['tax']}")
print(f"Net Salary  : Rs. {n_salary}")
print("=" * 40)