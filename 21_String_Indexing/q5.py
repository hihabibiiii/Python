# Question: Access and print the middle character of an odd-length string.
# The middle index is length // 2.
# Example:
#   Input: "Python" -> even length, try "abcde"
#   Input: "abcde"  -> middle index = 2, middle char = 'c'
#   Output: c

text = input("Enter an odd-length string: ")
if len(text) % 2 == 0:
    print("The string has an even length. Please enter an odd-length string.")
else:
    mid_index = len(text) // 2
    print("Middle character:", text[mid_index])
