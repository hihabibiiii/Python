# Question 15 (Hard):
# Ask the user to enter a paragraph (or multiple sentences).
# Count the frequency of each word (case-insensitive, ignoring punctuation)
# using a dictionary. Print the words sorted by frequency (highest first).

# Solution:
import string

print("Enter a paragraph (press Enter twice to finish):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

paragraph = " ".join(lines)

# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned = paragraph.translate(translator).lower()

words = cleaned.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Sort by frequency descending
sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

print("\nWord Frequency (sorted by count):")
print(f"{'Word':<20} {'Count':<10}")
print("-" * 30)
for word, count in sorted_freq:
    print(f"{word:<20} {count:<10}")

# Example Input:
#   To be or not to be that is the question to be answered
# Example Output:
#   be      3
#   to      3
#   ...
