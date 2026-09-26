# Question:
# Simulate an ATM PIN check.
# The correct PIN is 1234 (hardcoded).
# Ask the user to enter their PIN.
# Print 'Access Granted' if the PIN is correct,
# otherwise print 'Access Denied'.
#
# Example:
#   Input: 1234  -> Output: Access Granted
#   Input: 9999  -> Output: Access Denied

CORRECT_PIN = "1234"

entered_pin = input("Enter your ATM PIN: ")

if entered_pin == CORRECT_PIN:
    print("Access Granted")
else:
    print("Access Denied")
