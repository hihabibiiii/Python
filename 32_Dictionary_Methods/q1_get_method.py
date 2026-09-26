# Question 1 (Easy):
# Use the get() method to safely access a key in a dictionary.
# Use a default value so that no KeyError is raised if the key doesn't exist.

# Solution:
person = {
    "name": "Alice",
    "age": 25,
    "city": "Boston"
}

# Safe access with get()
name = person.get("name", "Unknown")
email = person.get("email", "No email on file")  # key doesn't exist

print(f"Name:  {name}")
print(f"Email: {email}")

# Ask user for a key to look up
key = input("\nEnter a key to look up: ").strip()
result = person.get(key, f"Key '{key}' not found")
print(f"Result: {result}")

# Example Input:  city
# Example Output: Result: Boston

# Example Input:  phone
# Example Output: Result: Key 'phone' not found
