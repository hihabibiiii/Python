# Question 3 (Easy):
# Start with a dictionary containing name and age.
# Add a new key-value pair: 'email' with a value of your choice.
# Print the updated dictionary.

# Solution:
person = {
    "name": "Carol",
    "age": 28
}

print("Before:", person)

person["email"] = "carol@example.com"

print("After:", person)

# Example Output:
# Before: {'name': 'Carol', 'age': 28}
# After:  {'name': 'Carol', 'age': 28, 'email': 'carol@example.com'}
