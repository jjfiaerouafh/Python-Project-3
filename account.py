#BANK ACCOUNT SYSTEM
class BankAccount:
    
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


# Creating object
account1 = BankAccount("Anantha Krishnan", 123456789, 50000000)

# Calling methods
account1.display_balance()
account1.deposit(2000)
account1.withdraw(1500)
account1.display_balance()