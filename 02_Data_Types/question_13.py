# Question 13 (Hard):
# Show that Python is dynamically typed by reassigning the same variable
# to values of different types: int, str, float, list, dict.
# Print the type of the variable after each assignment.

# Solution:
data = 100
print("data =", data, "| Type:", type(data))

data = "Hello"
print("data =", data, "| Type:", type(data))

data = 3.14
print("data =", data, "| Type:", type(data))

data = [1, 2, 3]
print("data =", data, "| Type:", type(data))

data = {"key": "value"}
print("data =", data, "| Type:", type(data))

# Output:
# data = 100 | Type: <class 'int'>
# data = Hello | Type: <class 'str'>
# data = 3.14 | Type: <class 'float'>
# data = [1, 2, 3] | Type: <class 'list'>
# data = {'key': 'value'} | Type: <class 'dict'>
