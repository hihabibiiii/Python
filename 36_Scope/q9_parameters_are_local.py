# Question 9 (Medium):
# Show that function PARAMETERS are local to the function.
# Reassigning the parameter inside the function does NOT affect
# the variable passed from outside.

# Solution:
def try_to_change(name):
    print(f"  Inside function, name = '{name}'")
    name = "Changed!"    # reassigning local parameter
    print(f"  After reassignment inside, name = '{name}'")

original = "Alice"
print("Before function call, original =", original)
try_to_change(original)
print("After function call, original =", original)

# Integer example
def try_to_increment(n):
    print(f"  Inside function, n = {n}")
    n += 100
    print(f"  After += 100 inside function, n = {n}")

x = 5
print("\nBefore function call, x =", x)
try_to_increment(x)
print("After function call, x =", x)

# Conclusion
print("\nConclusion: reassigning parameters inside a function")
print("does NOT affect the original variable (immutable types).")

# Example Output:
# Before function call, original = Alice
#   Inside function, name = 'Alice'
#   After reassignment inside, name = 'Changed!'
# After function call, original = Alice
