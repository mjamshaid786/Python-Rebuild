'''-----ATM MACHINE USING CLASS-----'''
class Atm:
    '''Defining Constructor Here'''
    def __init__(self):
        self.pin = []
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = int(input("""
        1. Type 1 for setting pin. 
        2. Type 2 for Cash Deposit.
        3. Type 3 for Withdraw.
        4. Type 4 for Checking Balance.
        5. Type 5 for exit: """))
        '''-----CALLING FUNCTIONS-----'''
        if user_input == 1:
            self.creat_pin()
        elif user_input == 2:
            self.cash_deposit()
        elif user_input == 3:
            self.cash_withdraw()
        elif user_input == 4:
            self.check_balance()
        else:
            print("Bye_Bye")

    '''-----Pin Setting Function-----'''
    def creat_pin (self):
        self.pin = int(input("Enter your pin: "))
        print("Pin set successfully !")

    '''-----Cash Deposit Funtion-----'''
    def cash_deposit(self):
        pin_check = int(input("Enter you Pin:"))
        if pin_check == self.pin:
            amount = int(input("Enter amount: "))
            self.balance += amount
            print("Amount Successfully Deposited")
        else:
            print("Invalid Pin")
    
    '''----Cash Withdraw Function-----'''
    def cash_withdraw(self):
        pin_check = int(input("Enter you Pin:"))
        if pin_check == self.pin:
            amount = int(input("Enter amount: "))
            if amount < self.balance:
                self.balance -= amount
                print("Amount Successfully Withdrawn")
            else:
                print("Insufficient Balance !")
        else:
            print("Invalid Pin")
    
    '''-----Check Balance Function-----'''
    def check_balance(self):
        pin_check = int(input("Enter you Pin:"))
        if pin_check == self.pin:
            print(f"Your Balance is: {self.balance}")
