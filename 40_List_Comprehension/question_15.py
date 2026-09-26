# Question:
# Given a list of student dictionaries with 'name' and 'score',
# use list comprehension to extract names of students who passed (score >= 50).

students = [
    {"name": "Alice",   "score": 85},
    {"name": "Bob",     "score": 42},
    {"name": "Charlie", "score": 91},
    {"name": "Diana",   "score": 38},
    {"name": "Eve",     "score": 67},
    {"name": "Frank",   "score": 50},
]

print("All students:")
for s in students:
    print(f"  {s['name']}: {s['score']}")

passed = [s["name"] for s in students if s["score"] >= 50]
print(f"\nStudents who passed (score >= 50): {passed}")
