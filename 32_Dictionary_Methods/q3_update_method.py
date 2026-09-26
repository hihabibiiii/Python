# Question 3 (Easy):
# Start with a base dictionary. Use update() to:
#   (a) Add new key-value pairs from another dictionary
#   (b) Update existing values
# Print the dictionary before and after each update.

# Solution:
profile = {
    "name": "Carol",
    "age": 30,
    "city": "Austin"
}
print("Original:", profile)

# (a) Update with new keys
extras = {"hobby": "Reading", "language": "Python"}
profile.update(extras)
print("After adding new keys:", profile)

# (b) Update existing value
profile.update({"age": 31, "city": "Denver"})
print("After updating existing keys:", profile)

# Example Output:
# Original: {'name': 'Carol', 'age': 30, 'city': 'Austin'}
# After adding new keys: {'name': 'Carol', 'age': 30, 'city': 'Austin', 'hobby': 'Reading', 'language': 'Python'}
# After updating existing keys: {'name': 'Carol', 'age': 31, 'city': 'Denver', 'hobby': 'Reading', 'language': 'Python'}
