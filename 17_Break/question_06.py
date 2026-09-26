# Question:
# Find the first number in the range 1 to 1000 that is divisible by both 7 AND 11.
# Use break when found.

# Example Output:
# First number divisible by 7 and 11: 77

for num in range(1, 1001):
    if num % 7 == 0 and num % 11 == 0:
        print(f"First number divisible by 7 and 11: {num}")
        break
