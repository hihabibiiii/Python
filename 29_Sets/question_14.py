# Question:
# Take a sentence from the user.
# Find all unique words in the sentence using a set.
# Print the unique words and count.

# Example:
# Enter a sentence: the cat sat on the mat the
# Unique words: {'the', 'cat', 'sat', 'on', 'mat'}
# Count: 5

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

unique_words = set(words)
print(f"Total words: {len(words)}")
print(f"Unique words: {unique_words}")
print(f"Unique word count: {len(unique_words)}")
