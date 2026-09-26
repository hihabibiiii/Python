# Question: Implement retry logic using a loop and try/except.
# Keep asking the user to enter a valid integer until they do.
# Once a valid integer is entered, print it and exit the loop.

# Example:
# Enter a whole number: hello
# Invalid input! 'hello' is not an integer. Please try again.
# Enter a whole number: 3.5
# Invalid input! '3.5' is not an integer. Please try again.
# Enter a whole number: 42
# Great! You entered the valid integer: 42

while True:
    user_input = input("Enter a whole number: ")
    try:
        number = int(user_input)
        print(f"Great! You entered the valid integer: {number}")
        break  # Exit the loop on success
    except ValueError:
        print(f"Invalid input! '{user_input}' is not an integer. Please try again.")
