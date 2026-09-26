# Question 13 (Hard):
# Demonstrate that a FOR LOOP variable is accessible AFTER the loop ends
# (unlike some other languages). Python for-loop variables "leak" into
# the enclosing scope.

# Solution:
# After a for loop, the loop variable still exists
for i in range(5):
    pass

print("Loop variable 'i' after loop:", i)   # prints 4

# Practical consequence: last item of list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    pass

print("Last fruit iterated:", fruit)   # prints 'cherry'

# Inside a function
def loop_scope():
    for num in range(1, 6):
        squared = num ** 2
    # Both 'num' and 'squared' still exist here
    print(f"After loop: num = {num}, squared = {squared}")

loop_scope()

# Inside a list comprehension — variable does NOT leak (Python 3 behavior)
result = [x * 2 for x in range(5)]
try:
    print("Comprehension variable x:", x)
except NameError:
    print("Comprehension variable 'x' is NOT accessible outside comprehension.")

# Example Output:
# Loop variable 'i' after loop: 4
# Last fruit iterated: cherry
