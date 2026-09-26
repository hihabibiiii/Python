# Question 5 (Easy):
# Demonstrate membership operators `in` and `not in`
# with a list and a string.

# Solution:
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
print("'banana' in fruits     :", "banana" in fruits)
print("'grape' in fruits      :", "grape" in fruits)
print("'grape' not in fruits  :", "grape" not in fruits)

sentence = "Hello, Python world!"
print("\nString:", sentence)
print("'Python' in sentence   :", "Python" in sentence)
print("'Java' in sentence     :", "Java" in sentence)
print("'Java' not in sentence :", "Java" not in sentence)

# Output:
# List: ['apple', 'banana', 'cherry']
# 'banana' in fruits     : True
# 'grape' in fruits      : False
# 'grape' not in fruits  : True
#
# String: Hello, Python world!
# 'Python' in sentence   : True
# 'Java' in sentence     : False
# 'Java' not in sentence : True
