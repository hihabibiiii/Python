# Question:
# Use a lambda with sorted() to sort a list of strings by their length.

words = ["banana", "kiwi", "apple", "fig", "elderberry", "grape"]
print(f"Original: {words}")

sorted_words = sorted(words, key=lambda s: len(s))
print(f"Sorted by length: {sorted_words}")
