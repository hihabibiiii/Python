# Question:
# Keep reading numbers from the user.
# Use break when the user enters a number that was already entered before (duplicate detected).
# Print the duplicate number.

# Example:
# Enter a number: 5
# Enter a number: 3
# Enter a number: 8
# Enter a number: 3
# Duplicate detected: 3

seen = []
while True:
    num = int(input("Enter a number: "))
    if num in seen:
        print(f"Duplicate detected: {num}")
        break
    seen.append(num)

print(f"Numbers entered before duplicate: {seen}")
