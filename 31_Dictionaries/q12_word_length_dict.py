# Question 12 (Hard):
# Ask the user to enter a sentence.
# Split it into words and create a dictionary where:
#   - Key = word
#   - Value = length of that word
# Print the resulting dictionary.

# Solution:
sentence = input("Enter a sentence: ").strip()

words = sentence.split()
word_lengths = {}
for word in words:
    # Strip punctuation for cleaner keys
    clean_word = word.strip(".,!?;:\"'")
    word_lengths[clean_word] = len(clean_word)

print("\nWord lengths dictionary:")
for word, length in word_lengths.items():
    print(f"  '{word}': {length}")

# Example Input:  Hello world this is Python
# Example Output:
# Word lengths dictionary:
#   'Hello': 5
#   'world': 5
#   'this': 4
#   'is': 2
#   'Python': 6
