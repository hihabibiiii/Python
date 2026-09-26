# Question 10 (Medium):
# Given two lists — one of keys and one of values — create a dictionary
# by combining them using zip(). Print the resulting dictionary.

# Solution:
keys = ["name", "age", "country", "language", "hobby"]
values = ["Grace", 27, "Canada", "Python", "Painting"]

combined = dict(zip(keys, values))
print("Dictionary from two lists:")
print(combined)

# Demonstrate individual access
print("\nAccessing individual items:")
for k, v in combined.items():
    print(f"  {k}: {v}")

# Example Output:
# Dictionary from two lists:
# {'name': 'Grace', 'age': 27, 'country': 'Canada', 'language': 'Python', 'hobby': 'Painting'}
#
# Accessing individual items:
#   name: Grace
#   age: 27
#   country: Canada
#   language: Python
#   hobby: Painting
