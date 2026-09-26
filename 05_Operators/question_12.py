# Question 12 (Hard):
# Use the walrus operator (:=) inside a while loop.
# Keep reading user input until the user types 'quit'.
# Process (print in uppercase) each non-quit input.

# Solution:
print("Type something and press Enter. Type 'quit' to stop.")

while (user_input := input("> ")) != "quit":
    print("You entered:", user_input.upper())

print("Loop ended. Goodbye!")

# Example Input / Output:
# Type something and press Enter. Type 'quit' to stop.
# > hello
# You entered: HELLO
# > python is cool
# You entered: PYTHON IS COOL
# > quit
# Loop ended. Goodbye!
