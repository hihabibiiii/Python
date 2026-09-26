# Question: Demonstrate catching a NameError, which occurs when you try to use
# a variable that has not been defined.
# Use try/except to catch the NameError and print a helpful message.

# Note: NameError example — using a variable before defining it.

# Example output:
# Trying to use 'total' before defining it...
# Error caught: name 'total' is not defined
# Now defining total = 100
# Total is: 100

print("Trying to use 'total' before defining it...")

try:
    # This will raise NameError because 'total' is not defined yet
    print(f"Total is: {total}")
except NameError as e:
    print(f"Error caught: {e}")

# Now define the variable properly
print("Now defining total = 100")
total = 100
print(f"Total is: {total}")
