# Question:
# Write a recursive function to check if a string is a palindrome.
# A palindrome reads the same forwards and backwards.

# Example:
# Enter a string: racecar
# 'racecar' is a palindrome: True

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

text = input("Enter a string: ").replace(" ", "").lower()
result = is_palindrome(text)
print(f"'{text}' is a palindrome: {result}")
