# Question: Check if a string is a palindrome using slicing.
# A palindrome reads the same forwards and backwards.
# Compare the string with its reverse using [::-1].
# Example:
#   Input: "racecar" -> Output: 'racecar' is a palindrome!
#   Input: "hello"   -> Output: 'hello' is NOT a palindrome.

text = input("Enter a string: ")
if text == text[::-1]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is NOT a palindrome.")
