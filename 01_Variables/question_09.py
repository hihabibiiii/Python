# Question 9 (Medium):
# Create a variable `my_var = 42`.
# Delete it using the `del` statement.
# Verify it is gone by attempting to access it inside a try/except block
# that catches NameError, and print an appropriate message.

# Solution:
my_var = 42
print("Before deletion, my_var =", my_var)

del my_var

try:
    print(my_var)
except NameError:
    print("my_var has been deleted and no longer exists.")

# Output:
# Before deletion, my_var = 42
# my_var has been deleted and no longer exists.
