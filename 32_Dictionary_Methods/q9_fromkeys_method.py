# Question 9 (Medium):
# Use the fromkeys() class method to create a new dictionary.
# Set all keys to the same default value.
# Demonstrate with different examples.

# Solution:

# Example 1: Create a dict with default value 0
subjects = ["Math", "Science", "English", "History"]
scores = dict.fromkeys(subjects, 0)
print("Subjects with default score of 0:")
print(scores)

# Example 2: Default value is None
fields = ["username", "email", "password", "phone"]
user_form = dict.fromkeys(fields)      # None is default when no value given
print("\nUser form template (all None):")
print(user_form)

# Example 3: Create from a string (each unique character as key)
template = dict.fromkeys("hello", False)
print("\nDict from string 'hello' with default False:")
print(template)

# Example Output:
# Subjects with default score of 0:
# {'Math': 0, 'Science': 0, 'English': 0, 'History': 0}
#
# User form template (all None):
# {'username': None, 'email': None, 'password': None, 'phone': None}
