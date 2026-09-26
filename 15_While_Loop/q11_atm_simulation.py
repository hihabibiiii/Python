# Question:
# Simulate an ATM machine using a while loop.
# Starting balance = 10,000.
# Keep asking the user for a withdrawal amount.
# - If amount = 0: exit the ATM.
# - If amount > balance: print 'Insufficient funds!'
# - If amount <= balance: deduct and show remaining balance.
# Stop when balance runs out or user enters 0.
#
# Example:
#   Balance: 10000
#   Withdraw: 3000  -> Remaining: 7000
#   Withdraw: 8000  -> Insufficient funds!
#   Withdraw: 0     -> Thank you. Goodbye!

balance = 10000.0
print("=== ATM Simulation ===")
print(f"Current balance: {balance:.2f}")

while balance > 0:
    amount = float(input("\nEnter withdrawal amount (0 to exit): "))
    if amount == 0:
        print("Thank you. Goodbye!")
        break
    if amount > balance:
        print(f"Insufficient funds! Your balance is {balance:.2f}")
    else:
        balance = balance - amount
        print(f"Withdrawal successful! Remaining balance: {balance:.2f}")

if balance == 0:
    print("Your balance is zero. Please visit a branch.")
