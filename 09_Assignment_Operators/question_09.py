# Question:
# Simulate a bank account using assignment operators.
# Starting balance = 1000.
# Perform the following transactions using += and -=:
#   Deposit: 500, Withdraw: 200, Deposit: 300, Withdraw: 800
# Print balance after each transaction.

balance = 1000
print(f"Initial balance: {balance}")

balance += 500
print(f"After deposit 500: {balance}")

balance -= 200
print(f"After withdrawal 200: {balance}")

balance += 300
print(f"After deposit 300: {balance}")

balance -= 800
print(f"After withdrawal 800: {balance}")

print(f"Final balance: {balance}")
