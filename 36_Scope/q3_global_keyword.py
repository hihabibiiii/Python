# Question 3 (Easy):
# Use the 'global' keyword to MODIFY a global variable from inside a function.
# Print the variable before and after the function call.

# Solution:
count = 0  # global variable
print("Before function call, count =", count)

def increment():
    global count       # declare intent to modify the global variable
    count += 1
    print("  Inside increment(), count =", count)

increment()
increment()
increment()

print("After 3 function calls, count =", count)

# Example Output:
# Before function call, count = 0
#   Inside increment(), count = 1
#   Inside increment(), count = 2
#   Inside increment(), count = 3
# After 3 function calls, count = 3
