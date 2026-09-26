# Question: Given a string, swap the first and last characters using indexing and concatenation.
# Example:
#   Input: "Python"
#   Output: nythoP

text = input("Enter a string: ")
if len(text) < 2:
    print("String must have at least 2 characters.")
else:
    # Build new string: last char + middle + first char
    swapped = text[-1] + text[1:-1] + text[0]
    print("Original string:", text)
    print("After swapping first and last characters:", swapped)
