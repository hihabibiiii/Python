# Question 14 (Hard):
# Demonstrate BUILT-IN scope: Python has built-in names like len, print, max.
# Show what happens if you accidentally shadow a built-in with a local variable.

# Solution:
# Normal use of built-in 'len'
my_list = [1, 2, 3, 4, 5]
print("Normal len():", len(my_list))

# --- DANGER: shadowing a built-in ---
def bad_practice():
    len = 999   # shadows the built-in 'len' inside this function!
    print("Inside function, 'len' is now:", len)

    # Now we can't use the real len() inside this function!
    try:
        result = len([1, 2, 3])   # TypeError: 'int' object is not callable
    except TypeError as e:
        print("TypeError:", e)
        print("Because 'len' was overwritten with an integer.")

bad_practice()

# Built-in 'len' is still fine outside bad_practice()
print("After bad_practice(), len([1,2,3]) =", len([1, 2, 3]))

# Moral of the story:
print("\n*** Never shadow built-in names! ***")
print("Avoid naming variables: list, len, max, min, print, input, etc.")

# Example Output:
# Normal len(): 5
# Inside function, 'len' is now: 999
# TypeError: 'int' object is not callable
