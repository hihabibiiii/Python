# Question:
# Take a string from the user.
# Check if the string contains ONLY digits (numeric string).
# Use a loop and isdigit() for each character.

# Example:
# Enter a string: 12345
# The string contains only digits: True

# Enter a string: 123abc
# The string contains only digits: False

text = input("Enter a string: ")

all_digits = True
for ch in text:
    if not ch.isdigit():
        all_digits = False
        break

print(f"The string contains only digits: {all_digits}")
