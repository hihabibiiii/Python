# Question:
# Take a string from the user and count the number of vowels (a, e, i, o, u)
# in it using a for loop.
#
# Example:
#   Input:  Hello World
#   Output: Number of vowels: 3

text = input("Enter a string: ")

vowel_count = 0
for char in text:
    if char.lower() in "aeiou":
        vowel_count = vowel_count + 1

print(f"Number of vowels in '{text}': {vowel_count}")
