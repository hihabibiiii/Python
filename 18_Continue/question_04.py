# Question:
# Take a string from the user.
# Print only consonants (skip vowels using `continue`).
# Spaces should also be skipped.

# Example:
# Enter a string: Hello World
# Consonants: H l l W r l d

text = input("Enter a string: ")
vowels = "aeiouAEIOU"

print("Consonants: ", end="")
for ch in text:
    if ch in vowels or ch == " ":
        continue
    print(ch, end=" ")
print()
