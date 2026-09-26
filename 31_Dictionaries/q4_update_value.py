# Question 4 (Easy):
# Create a dictionary with name, age, and city.
# Update the value of 'city' to a new city.
# Print the dictionary before and after the update.

# Solution:
person = {
    "name": "David",
    "age": 35,
    "city": "Paris"
}

print("Before:", person)

person["city"] = "Berlin"

print("After:", person)

# Example Output:
# Before: {'name': 'David', 'age': 35, 'city': 'Paris'}
# After:  {'name': 'David', 'age': 35, 'city': 'Berlin'}
