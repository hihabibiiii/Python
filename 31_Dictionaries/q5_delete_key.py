# Question 5 (Easy):
# Create a dictionary with keys: name, age, city, phone.
# Delete the key 'phone' using the del statement.
# Print the dictionary before and after deletion.

# Solution:
contact = {
    "name": "Eve",
    "age": 22,
    "city": "Tokyo",
    "phone": "123-456-7890"
}

print("Before:", contact)

del contact["phone"]

print("After:", contact)

# Example Output:
# Before: {'name': 'Eve', 'age': 22, 'city': 'Tokyo', 'phone': '123-456-7890'}
# After:  {'name': 'Eve', 'age': 22, 'city': 'Tokyo'}
