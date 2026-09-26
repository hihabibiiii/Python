# Question 9 (Medium):
# Create two separate dictionaries (e.g. personal info and work info).
# Merge them into a single dictionary and print the merged result.

# Solution:
personal_info = {
    "name": "Frank",
    "age": 40,
    "city": "Sydney"
}

work_info = {
    "company": "TechCorp",
    "role": "Developer",
    "experience": 10
}

# Method 1: Using {**dict1, **dict2} (Python 3.5+)
merged = {**personal_info, **work_info}
print("Merged dictionary:", merged)

# Method 2: Using update() (modifies a copy)
merged2 = personal_info.copy()
merged2.update(work_info)
print("Merged (method 2):", merged2)

# Example Output:
# Merged dictionary: {'name': 'Frank', 'age': 40, 'city': 'Sydney',
#                     'company': 'TechCorp', 'role': 'Developer', 'experience': 10}
