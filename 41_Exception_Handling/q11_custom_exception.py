# Question: Create a custom exception class by inheriting from Exception.
# Create 'InsufficientFundsError' for a bank account scenario.
# Raise this custom exception when a withdrawal exceeds the balance,
# then catch and handle it.

# Example:
# Account balance: $500
# Attempting to withdraw $300... Success! Remaining balance: $200
# Attempting to withdraw $250... 
# Custom Error: InsufficientFundsError: Cannot withdraw $250. Only $200 available.

# Define a custom exception class
class InsufficientFundsError(Exception):
    """Raised when a withdrawal amount exceeds the account balance."""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw ${amount}. Only ${balance} available.")

# Bank account simulation
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

# Test the custom exception
balance = 500
print(f"Account balance: ${balance}")

try:
    balance = withdraw(balance, 300)
    print(f"Attempting to withdraw $300... Success! Remaining balance: ${balance}")
    balance = withdraw(balance, 250)
    print(f"Attempting to withdraw $250... Success! Remaining balance: ${balance}")
except InsufficientFundsError as e:
    print(f"Custom Error: {type(e).__name__}: {e}")
