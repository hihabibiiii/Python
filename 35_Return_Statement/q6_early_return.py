# Question 6 (Medium):
# Define a function called safe_divide that:
#   - Returns -1 if the divisor is 0 (early return for invalid input)
#   - Otherwise computes and returns the result of a / b

# Solution:
def safe_divide(a, b):
    if b == 0:
        return -1  # early return: guard clause
    return a / b

# Test cases
test_pairs = [(10, 2), (9, 3), (7, 0), (0, 5), (-12, 4)]
for a, b in test_pairs:
    result = safe_divide(a, b)
    if result == -1:
        print(f"safe_divide({a}, {b}) = ERROR: Division by zero")
    else:
        print(f"safe_divide({a}, {b}) = {result}")

# Get user input
a = float(input("\nEnter numerator: "))
b = float(input("Enter denominator: "))
result = safe_divide(a, b)
if result == -1:
    print("Cannot divide by zero!")
else:
    print(f"{a} / {b} = {result}")

# Example Output:
# safe_divide(10, 2) = 5.0
# safe_divide(7, 0)  = ERROR: Division by zero
