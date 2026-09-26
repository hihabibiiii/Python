# Question 12 (Hard):
# Given a dictionary of student names and scores, use a dictionary comprehension
# with items() to filter only students who scored more than 50.
# Print the filtered dictionary.

# Solution:
student_scores = {
    "Alice": 82,
    "Bob": 45,
    "Carol": 91,
    "David": 38,
    "Eve": 67,
    "Frank": 50,
    "Grace": 73
}

print("All students:")
for name, score in student_scores.items():
    status = "PASS" if score > 50 else "FAIL"
    print(f"  {name:<10}: {score}  [{status}]")

# Filter using dict comprehension with items()
passed = {name: score for name, score in student_scores.items() if score > 50}

print(f"\nStudents with score > 50:")
print(passed)

# Also demonstrate filtering by a different threshold
threshold = int(input("\nEnter a custom score threshold: "))
filtered = {name: score for name, score in student_scores.items() if score > threshold}
print(f"Students scoring above {threshold}: {filtered}")

# Example Output (threshold=70):
# Students scoring above 70: {'Alice': 82, 'Carol': 91, 'Grace': 73}
