# Question:
# You have a dictionary of names and scores.
# Use a lambda as a key for sorted() to sort the dictionary by value (score).
# Print the sorted results.

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95, "Eve": 88}
print("Original dictionary:", scores)

# Sort by value using lambda
sorted_items = sorted(scores.items(), key=lambda item: item[1])
print("\nSorted by score (ascending):")
for name, score in sorted_items:
    print(f"  {name}: {score}")
