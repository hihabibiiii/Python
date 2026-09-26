# Question:
# Compute the factorial of 5 using the *= operator inside a for loop.
# Start with result = 1 and multiply by each number from 1 to 5.

# Example Output:
# 5! = 120

result = 1
for i in range(1, 6):
    result *= i

print(f"5! = {result}")
