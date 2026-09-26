# Question 1 (Easy):
# Define a function called add that takes two numbers as arguments
# and RETURNS their sum. Print the result after calling the function.

# Solution:
def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)
print("10 + 25 =", add(10, 25))
print("(-7) + 4 =", add(-7, 4))

# Get values from user
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
print(f"{a} + {b} = {add(a, b)}")

# Example Input:  12, 8
# Example Output: 12.0 + 8.0 = 20.0
