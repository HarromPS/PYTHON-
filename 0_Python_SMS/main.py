# Python programming to create a banking system


class Account:

    def __init__(self):
        self.balance = 0
        print("Your Account is created\n")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: \nRs."))
        self.balance += amount
        print("Your New balance \nRs.", amount)

    def withdraw(self):
        amount = float(input("Enter the amount to withhdraw\nRs."))
        if (amount > self.balance):
            print("Insufficient Balance \n")

        else:
            self.balance -= amount
            print("Your remaining balance is \nRs.", amount)

    def enquiry(self):
        print("Your Total Balance:\n\Rs.", self.balance)


user = Account


account = Account()
account.deposit()
account.withdraw()
account.enquiry()
