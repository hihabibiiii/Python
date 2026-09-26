# Question:
# Keep asking the user to enter a number.
# Stop and exit the loop when the user enters -1.
# Print the sum of all entered numbers (excluding -1).

# Example:
# Enter a number (-1 to stop): 5
# Enter a number (-1 to stop): 8
# Enter a number (-1 to stop): -1
# Sum = 13

total = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    total += num

print(f"Sum = {total}")
