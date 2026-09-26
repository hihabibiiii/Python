# Question:
# Use map() to extract a specific field from a list of tuples.
# Given a list of (name, age, score) tuples, extract only the names.

students = [
    ("Alice", 20, 85),
    ("Bob", 22, 92),
    ("Charlie", 21, 78),
    ("Diana", 23, 95),
]

print("Student records:", students)

names = list(map(lambda s: s[0], students))
print(f"Names: {names}")

scores = list(map(lambda s: s[2], students))
print(f"Scores: {scores}")
