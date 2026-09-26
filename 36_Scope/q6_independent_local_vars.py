# Question 6 (Medium):
# Create TWO functions, each with a LOCAL variable named x.
# Show that they are completely independent of each other.

# Solution:
def function_a():
    x = 100     # local to function_a
    print("Inside function_a, x =", x)
    x += 50
    print("After modifying inside function_a, x =", x)

def function_b():
    x = 999     # local to function_b; completely separate from function_a's x
    print("Inside function_b, x =", x)
    x -= 100
    print("After modifying inside function_b, x =", x)

# Call both functions
function_a()
print()
function_b()
print()
function_a()   # function_a's x is always reset to 100 on each call

# Example Output:
# Inside function_a, x = 100
# After modifying inside function_a, x = 150

# Inside function_b, x = 999
# After modifying inside function_b, x = 899

# Inside function_a, x = 100     <-- starts fresh each call
# After modifying inside function_a, x = 150
