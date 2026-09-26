# Question 7 (Medium):
# Show the difference between mutable (list) and immutable (tuple).
# Modify an element of a list — it should work fine.
# Attempt to modify an element of a tuple — catch the error using try/except.

# Solution:
my_list = [10, 20, 30]
print("Original list:", my_list)
my_list[0] = 99          # Lists are mutable — this works
print("Modified list:", my_list)

my_tuple = (10, 20, 30)
print("\nOriginal tuple:", my_tuple)
try:
    my_tuple[0] = 99     # Tuples are immutable — this raises TypeError
except TypeError as e:
    print("Error modifying tuple:", e)

# Output:
# Original list: [10, 20, 30]
# Modified list: [99, 20, 30]
#
# Original tuple: (10, 20, 30)
# Error modifying tuple: 'tuple' object does not support item assignment
