# Question 5 (Easy):
# Define a function that explicitly returns None.
# Show that functions without a return statement also return None.

# Solution:
def do_nothing():
    print("Function called, but returns None explicitly.")
    return None

def also_none():
    print("This function has no return statement.")

# Call and capture return values
result1 = do_nothing()
result2 = also_none()

print(f"\nReturn value of do_nothing(): {result1}")
print(f"Return value of also_none():  {result2}")
print(f"result1 is None: {result1 is None}")
print(f"result2 is None: {result2 is None}")

# Example Output:
# Function called, but returns None explicitly.
# This function has no return statement.
#
# Return value of do_nothing(): None
# Return value of also_none():  None
# result1 is None: True
# result2 is None: True
