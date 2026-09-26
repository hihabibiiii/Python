# Question: Check if the first and last characters of a string are the same.
# Use index 0 and -1 to compare.
# Example:
#   Input: "level"  -> Output: Yes, first and last characters are the same: 'l'
#   Input: "Python" -> Output: No, first 'P' and last 'n' are different.

text = input("Enter a string: ")
if text[0] == text[-1]:
    print(f"Yes, first and last characters are the same: '{text[0]}'")
else:
    print(f"No, first '{text[0]}' and last '{text[-1]}' are different.")
