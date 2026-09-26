# Question: Use the collections module: Counter, defaultdict, and OrderedDict.
# Demonstrate each with practical examples.

from collections import Counter, defaultdict, OrderedDict

print("=" * 50)
print("       collections Module Demo")
print("=" * 50)

# --- Counter ---
print("\n--- Counter ---")
sentence = "the quick brown fox jumps over the lazy dog the"
words = sentence.split()
word_count = Counter(words)
print(f"Text: '{sentence}'")
print(f"Word counts: {dict(word_count)}")
print(f"Most common 3 words: {word_count.most_common(3)}")

# Count characters
char_count = Counter("mississippi")
print(f"\nCharacter count in 'mississippi': {dict(char_count)}")

# --- defaultdict ---
print("\n--- defaultdict ---")
# defaultdict never raises KeyError — provides a default value
student_scores = defaultdict(list)
student_scores['Alice'].append(85)
student_scores['Alice'].append(90)
student_scores['Bob'].append(78)
student_scores['Charlie'].append(92)

print("Student scores (using defaultdict of lists):")
for student, scores in student_scores.items():
    avg = sum(scores) / len(scores)
    print(f"  {student}: {scores} → Average: {avg:.1f}")

# Accessing a key that doesn't exist returns default (empty list)
print(f"  Diana (not added yet): {student_scores['Diana']}")

# --- OrderedDict ---
print("\n--- OrderedDict ---")
# OrderedDict remembers insertion order (regular dicts do too in Python 3.7+)
# But OrderedDict has extra features like move_to_end()
rankings = OrderedDict()
rankings['Gold'] = 'Alice'
rankings['Silver'] = 'Bob'
rankings['Bronze'] = 'Charlie'

print("Medal rankings:")
for medal, name in rankings.items():
    print(f"  {medal}: {name}")

# Move 'Silver' to the end
rankings.move_to_end('Silver')
print("\nAfter moving Silver to end:")
for medal, name in rankings.items():
    print(f"  {medal}: {name}")
