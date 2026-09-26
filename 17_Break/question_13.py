# Question:
# Find the first perfect number between 1 and 10000.
# A perfect number equals the sum of its proper divisors.
# (e.g., 6 = 1+2+3)
# Use break when found.

# Example Output:
# First perfect number: 6

for num in range(2, 10001):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        print(f"First perfect number: {num}")
        break
