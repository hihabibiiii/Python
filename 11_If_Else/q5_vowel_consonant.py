# Question:
# Take a single character from the user.
# Print 'Vowel' if it is a vowel (a, e, i, o, u),
# otherwise print 'Consonant'.
#
# Example:
#   Input: a  -> Output: Vowel
#   Input: b  -> Output: Consonant

char = input("Enter a single character: ").lower()

if char in "aeiou":
    print("Vowel")
else:
    print("Consonant")
