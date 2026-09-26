# Question:
# Use filter() to get strings longer than 4 characters from a list.

words = ["hi", "hello", "cat", "python", "ai", "world", "ok"]
print(f"Original: {words}")

long_words = list(filter(lambda w: len(w) > 4, words))
print(f"Words longer than 4 chars: {long_words}")
