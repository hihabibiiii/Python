# Question:
# Take a sentence and create a list of (word, length) tuples.
# Use list comprehension.

# Example:
# Sentence: "Python is fun"
# [('Python', 6), ('is', 2), ('fun', 3)]

sentence = input("Enter a sentence: ")
words = sentence.split()
word_lengths = [(word, len(word)) for word in words]

print("Word-length pairs:")
for pair in word_lengths:
    print(f"  {pair}")
