# Question:
# Simulate an ATM withdrawal using nested if.
# Take the current balance and withdrawal amount from the user.
# If the withdrawal amount <= balance:
#   - If the amount is a multiple of 100 (valid ATM denomination):
#     - Print 'Withdrawal successful' and show the new balance.
#   - Else: print 'Invalid amount! ATM dispenses multiples of 100 only.'
# If amount > balance:
#   - Print 'Insufficient funds!'
#
# Example:
#   balance=5000, amount=200  -> Withdrawal successful! Remaining: 4800
#   balance=5000, amount=250  -> Invalid amount! ATM dispenses multiples of 100 only.
#   balance=5000, amount=6000 -> Insufficient funds!

balance = float(input("Enter your current balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        balance = balance - amount
        print(f"Withdrawal successful! Remaining balance: {balance:.2f}")
    else:
        print("Invalid amount! ATM dispenses multiples of 100 only.")
else:
    print("Insufficient funds!")
