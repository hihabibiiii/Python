# Question 2 (Easy):
# Create a dictionary and demonstrate the keys(), values(), and items() methods.
# Print each one to see what they return.

# Solution:
student = {
    "name": "Bob",
    "grade": "A",
    "score": 95,
    "subject": "Python"
}

print("=== keys() ===")
print(student.keys())
for key in student.keys():
    print(f"  Key: {key}")

print("\n=== values() ===")
print(student.values())
for value in student.values():
    print(f"  Value: {value}")

print("\n=== items() ===")
print(student.items())
for key, value in student.items():
    print(f"  {key}: {value}")

# Example Output:
# === keys() ===
# dict_keys(['name', 'grade', 'score', 'subject'])
#   Key: name
#   Key: grade
#   ...
#
# === values() ===
# dict_values(['Bob', 'A', 95, 'Python'])
#   Value: Bob
#   ...
