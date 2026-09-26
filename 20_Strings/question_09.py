# Question:
# Take a string from the user.
# Convert it to a list of characters and then back to a string.
# Print both the list and the rejoined string.

# Example:
# Enter a string: hello
# List of chars: ['h', 'e', 'l', 'l', 'o']
# Rejoined string: hello

text = input("Enter a string: ")

char_list = list(text)
print(f"List of chars: {char_list}")

rejoined = "".join(char_list)
print(f"Rejoined string: {rejoined}")
