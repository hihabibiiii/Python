# Question 12 (Hard):
# Demonstrate positional-only parameters (/) and keyword-only parameters (*)
# in Python 3.8+.
# / forces preceding args to be positional-only.
# * forces following args to be keyword-only.

# Solution:

# Positional-only: x and y MUST be passed positionally
def add_positional_only(x, y, /):
    return x + y

print("Positional-only add:")
print(add_positional_only(3, 4))         # OK
# add_positional_only(x=3, y=4)          # Would raise TypeError

# Keyword-only: x and y MUST be passed with keywords
def add_keyword_only(*, x, y):
    return x + y

print("\nKeyword-only add:")
print(add_keyword_only(x=10, y=5))       # OK
# add_keyword_only(10, 5)               # Would raise TypeError

# Combined: a is positional-only, b is normal, c is keyword-only
def combined(a, /, b, *, c):
    print(f"a={a}, b={b}, c={c}")

print("\nCombined function calls:")
combined(1, 2, c=3)          # a positional, b positional or keyword, c keyword
combined(1, b=2, c=3)        # b as keyword is fine here

# Example Output:
# Positional-only add:
# 7
# Keyword-only add:
# 15
# Combined function calls:
# a=1, b=2, c=3
# a=1, b=2, c=3
