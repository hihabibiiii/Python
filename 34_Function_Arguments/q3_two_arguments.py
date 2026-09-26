# Question 3 (Easy):
# Define a function with TWO positional arguments.
# The function should take a name and age and print a description.

# Solution:
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person("Alice", 25)
describe_person("Bob", 30)

name = input("\nEnter name: ").strip()
age = int(input("Enter age: "))
describe_person(name, age)

# Example Input:  Carol, 22
# Example Output:
# Alice is 25 years old.
# Bob is 30 years old.
# Carol is 22 years old.
