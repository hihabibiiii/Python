# Question 5 (Easy):
# Convert a list to a tuple and a tuple to a list.
# Print each result and its type.

# Solution:
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list, "| Type:", type(my_list))

converted_tuple = tuple(my_list)
print("As tuple     :", converted_tuple, "| Type:", type(converted_tuple))

my_tuple = (10, 20, 30)
print("\nOriginal tuple:", my_tuple, "| Type:", type(my_tuple))

converted_list = list(my_tuple)
print("As list       :", converted_list, "| Type:", type(converted_list))

# Output:
# Original list: [1, 2, 3, 4, 5] | Type: <class 'list'>
# As tuple     : (1, 2, 3, 4, 5) | Type: <class 'tuple'>
# Original tuple: (10, 20, 30)   | Type: <class 'tuple'>
# As list       : [10, 20, 30]   | Type: <class 'list'>
