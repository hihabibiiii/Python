# Question 5 (Medium):
# Demonstrate the LEGB rule: Python searches for a name in this order:
#   L - Local scope
#   E - Enclosing function scope
#   G - Global scope
#   B - Built-in scope

# Solution:
# B - Built-in: len is a built-in
print("Built-in len([1,2,3]):", len([1, 2, 3]))

# G - Global
value = "global"

def outer():
    # E - Enclosing scope for inner()
    value = "enclosing"

    def inner():
        # L - Local
        value = "local"
        print("  inner() sees 'local':", value)

    inner()
    print("outer() sees 'enclosing':", value)

outer()
print("Module level sees 'global':", value)

# Demonstrate LEGB lookup when no local binding exists
number = 42  # global

def outer2():
    number = 99  # enclosing

    def inner2():
        # inner2 has no local 'number' -> looks in enclosing -> finds 99
        print("  inner2() finds number in enclosing scope:", number)

    inner2()

outer2()

# Example Output:
# inner() sees 'local': local
# outer() sees 'enclosing': enclosing
# Module level sees 'global': global
