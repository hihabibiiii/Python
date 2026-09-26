# Question 14 (Hard):
# Check the type of a variable and process it differently depending on its type.
# If the value is an int, double it.
# If the value is a str, convert it to uppercase.
# Use if/else with type() — no def or lambda.

# Solution:
# Test with an integer
value = 7
if type(value) == int:
    processed = value * 2
    print(f"Integer detected. Doubled: {processed}")
elif type(value) == str:
    processed = value.upper()
    print(f"String detected. Uppercased: {processed}")
else:
    print("Unknown type:", type(value))

# Test with a string
value = "python"
if type(value) == int:
    processed = value * 2
    print(f"Integer detected. Doubled: {processed}")
elif type(value) == str:
    processed = value.upper()
    print(f"String detected. Uppercased: {processed}")
else:
    print("Unknown type:", type(value))

# Output:
# Integer detected. Doubled: 14
# String detected. Uppercased: PYTHON
