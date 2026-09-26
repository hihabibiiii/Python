# Question:
# Given a list of numbers, create a list of strings like ['num_1', 'num_2', ...]
# using list comprehension.

numbers = [1, 2, 3, 4, 5]
labels = [f"num_{n}" for n in numbers]
print(f"Original: {numbers}")
print(f"Labels:   {labels}")
