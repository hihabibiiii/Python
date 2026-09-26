# Question 1 (Easy):
# Demonstrate LOCAL scope: create a variable inside a function.
# Show that trying to access it outside the function causes a NameError.

# Solution:
def my_function():
    local_var = "I am local!"  # only accessible inside my_function
    print("Inside function:", local_var)

my_function()

# Trying to access local_var outside the function:
try:
    print("Outside function:", local_var)
except NameError as e:
    print(f"NameError caught: {e}")
    print("Confirmed: local_var is NOT accessible outside the function.")

# Example Output:
# Inside function: I am local!
# NameError caught: name 'local_var' is not defined
# Confirmed: local_var is NOT accessible outside the function.
