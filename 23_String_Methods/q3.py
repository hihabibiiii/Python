# Question: Use replace() to replace a specific word in a sentence.
# replace(old, new) returns a new string with all occurrences of 'old' replaced by 'new'.
# Example:
#   Sentence: "I love cats. Cats are great."
#   Replace: "cats" with "dogs"
#   Output: "I love dogs. Cats are great."  (case-sensitive)

sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

result = sentence.replace(old_word, new_word)
print("Updated sentence:", result)
