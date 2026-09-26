# Question:
# Take a single character from the user.
# Classify it as:
#   - Uppercase letter (A-Z)
#   - Lowercase letter (a-z)
#   - Digit (0-9)
#   - Special character (anything else)
#
# Example:
#   Input: A  -> Output: Uppercase letter
#   Input: g  -> Output: Lowercase letter
#   Input: 5  -> Output: Digit
#   Input: @  -> Output: Special character

char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
elif char.isupper():
    print("Uppercase letter")
elif char.islower():
    print("Lowercase letter")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")
