# Question:
# You have a list of tuples: (name, score).
# Use a lambda with sorted() to sort the list by score (second element).

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95), ("Eve", 88)]
print("Original:", students)

sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by score:", sorted_students)

sorted_desc = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted descending:", sorted_desc)
