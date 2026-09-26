# Question:
# Keep asking the user to enter a number.
# Stop when the user enters 0.
# Print the sum of all entered numbers (not including 0).
#
# Example:
#   Enter: 5, 10, 3, 7, 0
#   Output: Sum = 25

total = 0
print("Enter numbers one by one. Enter 0 to stop.")

number = int(input("Enter a number: "))
while number != 0:
    total = total + number
    number = int(input("Enter a number: "))

print(f"\nTotal sum of entered numbers: {total}")
