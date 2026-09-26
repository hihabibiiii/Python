# Question 8 (Medium):
# Define a function called reverse_string that takes a string as input
# and returns the reversed version of it.

# Solution:
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# Test with examples
test_strings = ["hello", "Python", "12345", "racecar", ""]
for s in test_strings:
    print(f"reverse_string('{s}') = '{reverse_string(s)}'")

# Get string from user
user_string = input("\nEnter a string to reverse: ")
print(f"Reversed: '{reverse_string(user_string)}'")

# Example Input:  OpenAI
# Example Output: Reversed: 'IAnepO'
