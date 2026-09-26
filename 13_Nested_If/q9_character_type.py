# Question:
# Take a single character from the user.
# If it's a letter (alphabetic):
#   - Check if it's uppercase or lowercase.
# If it's NOT a letter:
#   - Check if it's a digit or a special character.
#
# Example:
#   Input: A  -> Letter -> Uppercase
#   Input: g  -> Letter -> Lowercase
#   Input: 5  -> Not a letter -> Digit
#   Input: @  -> Not a letter -> Special character

char = input("Enter a single character: ")

if char.isalpha():
    if char.isupper():
        print(f"'{char}' is a Letter -> Uppercase")
    else:
        print(f"'{char}' is a Letter -> Lowercase")
else:
    if char.isdigit():
        print(f"'{char}' is Not a letter -> Digit")
    else:
        print(f"'{char}' is Not a letter -> Special character")
