# Question 10 (Medium):
# Define a function called power that takes a base and an exponent
# and returns base raised to the power of exponent.
# Do NOT use the ** operator — implement manually with a loop.

# Solution:
def power(base, exp):
    if exp == 0:
        return 1
    result = 1
    for _ in range(abs(exp)):
        result *= base
    if exp < 0:
        return 1 / result
    return result

# Test with examples
print(f"power(2, 10) = {power(2, 10)}")
print(f"power(3, 4)  = {power(3, 4)}")
print(f"power(5, 0)  = {power(5, 0)}")
print(f"power(2, -3) = {power(2, -3)}")

# Get inputs from user
base = float(input("\nEnter base: "))
exp = int(input("Enter exponent: "))
print(f"{base} ^ {exp} = {power(base, exp)}")

# Example Input:  2, 8
# Example Output: 2.0 ^ 8 = 256.0
