# Question 10 (Medium):
# Use **kwargs to build a profile dictionary from keyword arguments.
# The function should return the dictionary built from kwargs.

# Solution:
def build_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

# Build different profiles
user1 = build_profile(name="Alice", age=25, role="Engineer", city="London")
print("User 1 profile:")
for k, v in user1.items():
    print(f"  {k}: {v}")

user2 = build_profile(username="bob99", email="bob@example.com", active=True)
print("\nUser 2 profile:")
for k, v in user2.items():
    print(f"  {k}: {v}")

# Example Output:
# User 1 profile:
#   name: Alice
#   age: 25
#   role: Engineer
#   city: London
