# Question 8 (Medium):
# Demonstrate the 'nonlocal' keyword in nested functions.
# Use nonlocal to modify an enclosing function's variable.

# Solution:
def outer():
    total = 0    # enclosing variable

    def add(amount):
        nonlocal total   # refer to enclosing 'total', not create a new local
        total += amount
        print(f"  Added {amount}. Running total = {total}")

    add(10)
    add(25)
    add(5)
    print(f"Final total in outer(): {total}")

outer()

# Without nonlocal, the inner function would create a local variable
def outer_without_nonlocal():
    total = 0

    def add_wrong(amount):
        total = amount  # creates a NEW local variable 'total', does NOT modify enclosing
        print(f"  local total inside add_wrong = {total}")

    add_wrong(10)
    print(f"outer total unchanged: {total}")

print()
outer_without_nonlocal()

# Example Output:
#   Added 10. Running total = 10
#   Added 25. Running total = 35
#   Added 5. Running total = 40
# Final total in outer(): 40
