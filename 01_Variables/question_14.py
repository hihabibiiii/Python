# Question 14 (Hard):
# Demonstrate variable shadowing in Python.
# Create a variable x = 100 at the outer (module) level.
# Then use a for loop where the loop variable is also named x.
# Print x inside the loop and after the loop to show that
# the loop variable shadows and then overwrites the outer x.

# Solution:
x = 100
print("Before loop, x =", x)

# Inside the loop, x is rebound to each loop value (shadowing outer x)
for x in [200, 300, 400]:
    print("Inside loop, x =", x)

# After the loop, x retains the last loop value
print("After loop, x =", x)

# Note: In Python, for-loop variables leak into the enclosing scope.
# To truly protect outer_x, rename it or use a different loop variable.

# Output:
# Before loop, x = 100
# Inside loop, x = 200
# Inside loop, x = 300
# Inside loop, x = 400
# After loop, x = 400
