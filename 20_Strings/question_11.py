# Question:
# Take a sentence from the user.
# Count the number of words in the sentence.
# (Split by spaces and count parts.)

# Example:
# Enter a sentence: Python is a great language
# Word count: 5

sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Word count: {len(words)}")
