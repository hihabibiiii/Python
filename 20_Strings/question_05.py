# Question:
# Take a string from the user.
# Print each character of the string on a separate line with its index.

# Example:
# Enter a string: Hi
# 0: H
# 1: i

text = input("Enter a string: ")

for i, ch in enumerate(text):
    print(f"{i}: {ch}")
