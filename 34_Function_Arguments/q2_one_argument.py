# Question 2 (Easy):
# Define a function with ONE positional argument.
# The function should take a name and print a personalised message.

# Solution:
def introduce(name):
    print(f"Hi! My name is {name}.")

introduce("Alice")
introduce("Bob")

name = input("Enter your name: ").strip()
introduce(name)

# Example Input:  Charlie
# Example Output:
# Hi! My name is Alice.
# Hi! My name is Bob.
# Hi! My name is Charlie.
