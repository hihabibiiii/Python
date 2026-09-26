# Question:
# Take a string from the user.
# Print characters at even indices (0, 2, 4, ...) using a loop.

# Example:
# Enter a string: abcdefgh
# Characters at even indices: a c e g

text = input("Enter a string: ")

print("Characters at even indices: ", end="")
for i in range(0, len(text), 2):
    print(text[i], end=" ")
print()
