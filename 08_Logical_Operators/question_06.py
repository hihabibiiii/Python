# Question:
# Take a character from the user and check if it is a vowel (a, e, i, o, u).
# Use the `or` operator to check each vowel.

# Example:
# Enter a character: e
# e is a vowel.

ch = input("Enter a character: ").strip().lower()

if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is not a vowel.")
