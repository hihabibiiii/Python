# Question 4 (Easy):
# Take two number strings from the user using input().
# Convert each to an integer and print their sum.
# (This shows why we must cast input() results before arithmetic.)

# Solution:
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

num1 = int(num1_str)
num2 = int(num2_str)

total = num1 + num2
print("Sum:", total)

# Example Input / Output:
# Enter first number: 15
# Enter second number: 27
# Sum: 42
