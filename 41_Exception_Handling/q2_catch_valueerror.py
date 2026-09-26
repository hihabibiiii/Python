# Question: Ask the user to enter a number. Try to convert the input to an integer.
# Use try/except to catch a ValueError if the user enters a non-numeric string.
# Print an appropriate error message.

# Example:
# Enter a number: hello
# Error: 'hello' is not a valid integer!

# Enter a number: 42
# You entered: 42

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print(f"Error: '{user_input}' is not a valid integer!")
