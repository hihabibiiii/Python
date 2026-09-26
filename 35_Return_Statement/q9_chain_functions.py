# Question 9 (Medium):
# Demonstrate chaining function calls:
# Use the return value of one function as the input to another.

# Solution:
def double(n):
    return n * 2

def add_ten(n):
    return n + 10

def square(n):
    return n ** 2

# Chain function calls
x = 3
step1 = double(x)       # 3 * 2 = 6
step2 = add_ten(step1)  # 6 + 10 = 16
step3 = square(step2)   # 16^2 = 256

print(f"Starting value: {x}")
print(f"After double():   {step1}")
print(f"After add_ten():  {step2}")
print(f"After square():   {step3}")

# Chain in one line
result = square(add_ten(double(x)))
print(f"\nChained in one line: square(add_ten(double({x}))) = {result}")

# Get value from user
n = float(input("\nEnter a number: "))
print(f"square(add_ten(double({n}))) = {square(add_ten(double(n)))}")

# Example Input:  5
# Example Output: square(add_ten(double(5.0))) = 400.0
