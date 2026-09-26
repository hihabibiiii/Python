# Question 3 (Easy):
# Take two numbers from the user.
# Compare them and print which is greater, or if they are equal.

# Solution:
a = float(input("Enter first number : "))
b = float(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} and {b} are equal")

# Example:
# 8 vs 5  -> 8 is greater than 5
# 3 vs 3  -> 3 and 3 are equal
