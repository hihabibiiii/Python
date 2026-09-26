# Question:
# Use `pass` in an if/else block.
# If a number is negative, do nothing (pass).
# If it is non-negative, print it.

# Example:
# Enter a number: -3
# (nothing printed for negative)
# Enter a number: 7
# Number: 7

num = int(input("Enter a number: "))

if num < 0:
    pass  # No action needed for negative numbers
else:
    print(f"Number: {num}")
