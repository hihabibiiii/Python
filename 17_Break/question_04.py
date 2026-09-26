# Question:
# Read characters of a string one by one using a for loop.
# Use break when the first vowel is encountered.
# Print the vowel and its position.

# Example:
# Enter a string: Python
# First vowel: 'o' at index 4

text = input("Enter a string: ")
vowels = "aeiouAEIOU"

for i, ch in enumerate(text):
    if ch in vowels:
        print(f"First vowel: '{ch}' at index {i}")
        break
else:
    print("No vowel found in the string.")
