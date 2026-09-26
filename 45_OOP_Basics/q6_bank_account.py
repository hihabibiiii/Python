# Question: Create a class BankAccount with a balance attribute.
# Add methods deposit() and withdraw() with validation.

# Example output:
# Account created. Balance: $1000
# Deposited $500. New balance: $1500
# Withdrew $200. New balance: $1300
# Error: Insufficient funds!

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance:
            print("Error: Insufficient funds!")
            return
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        print(f"Account: {self.owner}, Balance: ${self.balance}")

# Test the BankAccount class
account = BankAccount("Alice", 1000)
account.get_balance()

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Should fail
account.get_balance()
