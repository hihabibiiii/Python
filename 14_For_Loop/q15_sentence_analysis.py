# Question:
# Take a sentence from the user.
# Using a for loop, find:
#   1. Total number of words
#   2. Total number of characters (excluding spaces)
#   3. The longest word in the sentence
#
# Example:
#   Input:  "The quick brown fox jumps"
#   Output:
#     Word count       : 5
#     Character count  : 20
#     Longest word     : jumps

sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = 0
char_count = 0
longest_word = ""

for word in words:
    word_count = word_count + 1
    char_count = char_count + len(word)
    if len(word) > len(longest_word):
        longest_word = word

print(f"\nWord count      : {word_count}")
print(f"Character count : {char_count} (excluding spaces)")
print(f"Longest word    : '{longest_word}' ({len(longest_word)} characters)")
