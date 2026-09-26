# Question:
# Compute the sum of squares of numbers from 1 to 10.
# Use the += operator inside a for loop.
# Formula: 1^2 + 2^2 + 3^2 + ... + 10^2

# Example Output:
# Sum of squares from 1 to 10 = 385

total = 0
for i in range(1, 11):
    total += i ** 2

print(f"Sum of squares from 1 to 10 = {total}")
