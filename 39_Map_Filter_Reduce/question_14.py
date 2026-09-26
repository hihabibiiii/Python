# Question:
# Use filter() to find all palindromes in a list of strings.

def is_palindrome(s):
    return s == s[::-1]

words = ["racecar", "hello", "madam", "python", "level", "world", "civic", "kayak"]
print(f"Words: {words}")

palindromes = list(filter(is_palindrome, words))
print(f"Palindromes: {palindromes}")
