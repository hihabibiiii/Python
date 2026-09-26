# Question 11 (Hard):
# Define a RECURSIVE function called factorial that returns n!
# Use the return statement to pass the result back up the call stack.

# Solution:
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Test
print(f"{'n':<5} {'n!'}")
print("-" * 15)
for i in range(0, 11):
    print(f"{i:<5} {factorial(i)}")

# Get number from user
n = int(input("\nEnter a non-negative integer: "))
if n < 0:
    print("Factorial not defined for negative numbers.")
else:
    print(f"{n}! = {factorial(n)}")

# Example Input:  8
# Example Output: 8! = 40320
