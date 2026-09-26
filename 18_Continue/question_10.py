# Question:
# Take a sentence from the user.
# Split it into words.
# Use `continue` to skip words with 4 or fewer characters.
# Print only words with more than 4 characters.

# Example:
# Enter a sentence: The quick brown fox jumped over lazy dogs
# Words longer than 4 characters: quick brown jumped

sentence = input("Enter a sentence: ")
words = sentence.split()

print("Words with more than 4 characters:")
for word in words:
    if len(word) <= 4:
        continue
    print(word, end=" ")
print()
