# Question 12 (Hard):
# Take input from the user and safely cast it to an integer.
# If the conversion fails (e.g. user enters letters), catch the ValueError
# and print a helpful error message instead of crashing.

# Solution:
user_input = input("Enter a whole number: ")

try:
    number = int(user_input)
    print(f"Successfully converted to int: {number}")
except ValueError:
    print(f"Error: '{user_input}' cannot be converted to an integer.")
    print("Please enter a valid whole number next time.")

# Example Input / Output 1 (valid input):
# Enter a whole number: 42
# Successfully converted to int: 42

# Example Input / Output 2 (invalid input):
# Enter a whole number: hello
# Error: 'hello' cannot be converted to an integer.
# Please enter a valid whole number next time.
