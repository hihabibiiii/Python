# Question:
# Take a string from the user and check if it is a palindrome.
# A palindrome reads the same forward and backward.
# (Ignore case and spaces.)

# Example:
# Enter a string: racecar
# "racecar" is a palindrome.

text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()

reversed_cleaned = ""
for ch in cleaned:
    reversed_cleaned = ch + reversed_cleaned

if cleaned == reversed_cleaned:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is NOT a palindrome.')
