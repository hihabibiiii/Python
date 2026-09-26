# Question 11 (Hard):
# Show that reassigning an IMMUTABLE argument (like an int) inside a function
# does NOT affect the outer variable.

# Solution:
def double_it(n):
    print(f"  Received n = {n}, id = {id(n)}")
    n = n * 2                    # n now points to a NEW integer object
    print(f"  After doubling, n = {n}, id = {id(n)}")
    return n

value = 10
print(f"Before: value = {value}, id = {id(value)}")

returned = double_it(value)

print(f"After function call: value = {value}")   # still 10
print(f"Returned value: {returned}")             # 20

# Same demonstration with strings (also immutable)
def add_exclamation(s):
    s = s + "!!!"   # creates a new string object
    print(f"  Inside function: '{s}'")

word = "Hello"
print(f"\nBefore: '{word}'")
add_exclamation(word)
print(f"After:  '{word}'")   # unchanged

# Example Output:
# Before: value = 10
# After function call: value = 10
# Returned value: 20
