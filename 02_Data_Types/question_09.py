# Question 9 (Medium):
# Demonstrate the None type:
#   - Create a variable and assign it None.
#   - Print its type.
#   - Check if it is None using `is None` and print the result.

# Solution:
result = None

print("Value:", result)
print("Type:", type(result))

if result is None:
    print("The variable is None.")
else:
    print("The variable has a value.")

# Output:
# Value: None
# Type: <class 'NoneType'>
# The variable is None.
