# Question:
# Take a sentence and create a list of the lengths of each word.
# Use list comprehension.

# Example:
# Sentence: "Python is really fun to learn"
# Lengths: [6, 2, 6, 3, 2, 5]

sentence = input("Enter a sentence: ")
words = sentence.split()
lengths = [len(word) for word in words]

print(f"Words:   {words}")
print(f"Lengths: {lengths}")
