# Question 2 (Easy):
# Start with the integer 100.
# Convert it to a float and then to a string.
# Print each result with its type.

# Solution:
integer_val = 100
print("Integer:", integer_val, "| Type:", type(integer_val))

float_val = float(integer_val)
print("Float  :", float_val, "| Type:", type(float_val))

string_val = str(integer_val)
print("String :", string_val, "| Type:", type(string_val))

# Output:
# Integer: 100 | Type: <class 'int'>
# Float  : 100.0 | Type: <class 'float'>
# String : 100 | Type: <class 'str'>
