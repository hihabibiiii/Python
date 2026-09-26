# Question 2 (Easy):
# Define a function called greet_person that takes a name as a parameter
# and prints a personalized greeting message.

# Solution:
def greet_person(name):
    print(f"Hello, {name}! Welcome to Python programming.")

# Call the function with different names
greet_person("Alice")
greet_person("Bob")

# Get name from user
name = input("\nEnter your name: ").strip()
greet_person(name)

# Example Input:  Charlie
# Example Output:
# Hello, Alice! Welcome to Python programming.
# Hello, Bob! Welcome to Python programming.
# Hello, Charlie! Welcome to Python programming.
