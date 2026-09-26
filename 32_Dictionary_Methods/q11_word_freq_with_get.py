# Question 11 (Hard):
# Ask the user to enter a sentence.
# Count word frequency using get() with a default of 0 to avoid KeyError.
# Print each word with its count.

# Solution:
sentence = input("Enter a sentence: ").strip().lower()

words = sentence.split()

word_count = {}
for word in words:
    # Clean punctuation
    clean = word.strip(".,!?;:\"'()")
    if clean:
        word_count[clean] = word_count.get(clean, 0) + 1

print("\nWord Frequency:")
print(f"{'Word':<20} {'Count'}")
print("-" * 28)
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{word:<20} {count}")

# Example Input:  the cat sat on the mat and the cat sat
# Example Output:
# Word Frequency:
# Word                 Count
# ----------------------------
# the                  3
# cat                  2
# sat                  2
# on                   1
# mat                  1
# and                  1
