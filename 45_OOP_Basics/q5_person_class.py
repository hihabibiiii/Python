# Question: Create a class Person with name and age, and a method introduce().
# The introduce() method prints a self-introduction message.

# Example output:
# Hi! My name is Alice and I am 30 years old.
# I am an adult.
# 
# Hi! My name is Tommy and I am 12 years old.
# I am a minor.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! My name is {self.name} and I am {self.age} years old.")
        if self.age >= 18:
            print("I am an adult.")
        else:
            print("I am a minor.")

# Create Person objects
person1 = Person("Alice", 30)
person1.introduce()

print()

person2 = Person("Tommy", 12)
person2.introduce()

print()

# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
user_person = Person(name, age)
user_person.introduce()
