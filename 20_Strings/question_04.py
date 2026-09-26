# Question:
# Take a sentence and a word from the user.
# Check if the word is present in the sentence using the `in` operator.

# Example:
# Enter a sentence: Python is awesome
# Enter a word to search: awesome
# 'awesome' is found in the sentence.

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print(f"'{word}' is found in the sentence.")
else:
    print(f"'{word}' is NOT found in the sentence.")
