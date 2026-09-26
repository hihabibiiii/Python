# Question:
# Use a lambda with max() and the key parameter to find the longest string in a list.

words = ["apple", "banana", "kiwi", "strawberry", "fig"]
print(f"Words: {words}")

longest = max(words, key=lambda s: len(s))
print(f"Longest word: '{longest}' (length {len(longest)})")
