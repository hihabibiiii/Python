# Question:
# Use the += operator to build a string character by character.
# Start with an empty string and add these characters one by one:
#   'H', 'e', 'l', 'l', 'o'
# Print the string after each addition.

word = ""

word += "H"
print(f"After adding H: '{word}'")

word += "e"
print(f"After adding e: '{word}'")

word += "l"
print(f"After adding l: '{word}'")

word += "l"
print(f"After adding l: '{word}'")

word += "o"
print(f"After adding o: '{word}'")

print(f"Final string: {word}")
