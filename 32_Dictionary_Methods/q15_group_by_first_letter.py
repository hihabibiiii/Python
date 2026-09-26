# Question 15 (Hard):
# Given a list of words, use setdefault() to group them by their first letter.
# Build a dictionary where:
#   - Key = first letter (uppercase)
#   - Value = list of words starting with that letter

# Solution:
words = [
    "apple", "avocado", "banana", "blueberry", "cherry",
    "apricot", "carrot", "broccoli", "corn", "almond",
    "beet", "celery", "asparagus"
]

grouped = {}

for word in words:
    first_letter = word[0].upper()
    grouped.setdefault(first_letter, []).append(word)

print("Words grouped by first letter:\n")
for letter in sorted(grouped.keys()):
    print(f"  {letter}: {grouped[letter]}")

# Ask user to add more words
print("\nEnter words to add (type 'done' to stop):")
while True:
    word = input("Word: ").strip().lower()
    if word == "done":
        break
    if word:
        first_letter = word[0].upper()
        grouped.setdefault(first_letter, []).append(word)

print("\nUpdated grouping:")
for letter in sorted(grouped.keys()):
    print(f"  {letter}: {grouped[letter]}")

# Example Output:
#   A: ['apple', 'avocado', 'apricot', 'almond', 'asparagus']
#   B: ['banana', 'blueberry', 'broccoli', 'beet']
#   C: ['cherry', 'carrot', 'corn', 'celery']
