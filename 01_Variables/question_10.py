# Question 10 (Medium):
# Assign a string to a variable named `data`.
# Reassign it to an integer, then to a float.
# After each assignment, print the value and its type using type().
# This demonstrates Python's dynamic typing.

# Solution:
data = "Hello, Python!"
print("Value:", data, "| Type:", type(data))

data = 42
print("Value:", data, "| Type:", type(data))

data = 3.14
print("Value:", data, "| Type:", type(data))

# Output:
# Value: Hello, Python! | Type: <class 'str'>
# Value: 42            | Type: <class 'int'>
# Value: 3.14          | Type: <class 'float'>
