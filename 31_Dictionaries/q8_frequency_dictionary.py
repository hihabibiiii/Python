# Question 8 (Medium):
# Ask the user to enter a word.
# Create a frequency dictionary that counts how many times each letter
# appears in the word. Print the resulting dictionary.

# Solution:
word = input("Enter a word: ").strip().lower()

freq = {}
for letter in word:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

print(f"\nLetter frequency in '{word}':")
for letter, count in freq.items():
    print(f"  '{letter}': {count}")

# Example Input:  banana
# Example Output:
# Letter frequency in 'banana':
#   'b': 1
#   'a': 3
#   'n': 2
