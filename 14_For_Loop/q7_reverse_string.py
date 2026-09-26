# Question:
# Take a string from the user and reverse it using a for loop.
# Do NOT use string slicing ([::-1]).
#
# Example:
#   Input:  hello
#   Output: olleh

text = input("Enter a string to reverse: ")

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

print(f"Reversed string: {reversed_text}")
