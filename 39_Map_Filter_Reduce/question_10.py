# Question:
# Use filter() to get words that start with a vowel from a list.

words = ["apple", "banana", "orange", "grape", "elderberry", "kiwi", "avocado"]
print(f"Original: {words}")

vowels = "aeiouAEIOU"
vowel_words = list(filter(lambda w: w[0] in vowels, words))
print(f"Words starting with a vowel: {vowel_words}")
