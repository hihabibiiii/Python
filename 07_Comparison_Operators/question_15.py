# Question 15 (Hard):
# Simulate a PIN verification system with 3 attempts.
# Store a correct PIN as a string variable.
# Ask the user to enter the PIN up to 3 times.
# Use comparison operators to check. No lists or loops needed — manual attempt logic.

# Solution:
stored_pin = "4829"   # The correct PIN (stored as string for leading-zero support)
print("=== PIN Verification ===")

# Attempt 1
pin = input("Enter PIN (Attempt 1/3): ")
if pin == stored_pin:
    print("Access GRANTED!")
else:
    print("Incorrect PIN.")

    # Attempt 2
    pin = input("Enter PIN (Attempt 2/3): ")
    if pin == stored_pin:
        print("Access GRANTED!")
    else:
        print("Incorrect PIN.")

        # Attempt 3
        pin = input("Enter PIN (Attempt 3/3): ")
        if pin == stored_pin:
            print("Access GRANTED!")
        else:
            print("Access DENIED. Too many failed attempts.")

# Example:
# Attempt 1: 1234 -> Incorrect
# Attempt 2: 0000 -> Incorrect
# Attempt 3: 4829 -> Access GRANTED!
