# Question 1 (Easy):
# Take two numbers from the user.
# Check if they are equal using == and print the result.

# Solution:
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))

if num1 == num2:
    print(f"{num1} and {num2} are equal.")
else:
    print(f"{num1} and {num2} are NOT equal.")

# Example:
# 5 == 5 -> equal
# 5 == 7 -> not equal
