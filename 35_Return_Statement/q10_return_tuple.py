# Question 10 (Medium):
# Define a function called divide_and_remainder that takes two integers a and b
# and returns a TUPLE containing the quotient and the remainder.

# Solution:
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # returns a tuple

# Test cases
pairs = [(10, 3), (20, 4), (17, 5), (100, 7)]
for a, b in pairs:
    q, r = divide_and_remainder(a, b)
    print(f"{a} ÷ {b} = {q} remainder {r}  (check: {b}*{q}+{r}={b*q+r})")

# Get user input
a = int(input("\nEnter dividend: "))
b = int(input("Enter divisor: "))
if b == 0:
    print("Cannot divide by zero!")
else:
    q, r = divide_and_remainder(a, b)
    print(f"{a} ÷ {b}: quotient = {q}, remainder = {r}")

# Example Input:  17, 5
# Example Output: 17 ÷ 5: quotient = 3, remainder = 2
