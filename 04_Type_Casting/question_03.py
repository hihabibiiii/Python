# Question 3 (Easy):
# Start with the float 3.99.
# Convert it to int (demonstrates truncation — NOT rounding).
# Also convert the float to a string.
# Print each result with its type.

# Solution:
float_val = 3.99
print("Float :", float_val, "| Type:", type(float_val))

int_val = int(float_val)  # Truncates decimal part
print("Int   :", int_val, "| Type:", type(int_val))
print("Note: int() truncates, it does NOT round. 3.99 becomes", int_val)

str_val = str(float_val)
print("String:", str_val, "| Type:", type(str_val))

# Output:
# Float : 3.99 | Type: <class 'float'>
# Int   : 3    | Type: <class 'int'>
# Note: int() truncates, it does NOT round. 3.99 becomes 3
# String: 3.99 | Type: <class 'str'>
