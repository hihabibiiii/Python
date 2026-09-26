# Question:
# You have a list of tuples: (name, score).
# Sort the list by the second element (score) in descending order.
# Print the sorted results.

# Example Output:
# Sorted by score (highest first):
# Diana    - 95
# Bob      - 92
# Alice    - 85
# Charlie  - 78

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]

# Sort by score (index 1), descending
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)

print("Sorted by score (highest first):")
for name, score in students_sorted:
    print(f"  {name:<10} - {score}")
