# Question 4 (Easy):
# Demonstrate identity operators `is` and `is not`.
# Compare: None, small integers (Python caches -5 to 256), and strings.

# Solution:
# None comparison
x = None
print("x is None    :", x is None)
print("x is not None:", x is not None)

# Small integer caching (Python reuses objects for small ints)
a = 5
b = 5
print("\na = 5, b = 5")
print("a is b :", a is b)    # True — same object in memory

# Large integers (not cached)
c = 1000
d = 1000
print("\nc = 1000, d = 1000")
print("c == d  :", c == d)   # True — same value
print("c is d  :", c is d)   # May be False — different objects

# Strings
s1 = "hello"
s2 = "hello"
print("\ns1 = 'hello', s2 = 'hello'")
print("s1 is s2 :", s1 is s2)  # Often True due to string interning

# Output (results can vary by Python implementation):
# x is None    : True
# x is not None: False
# a is b : True
# c == d  : True
# c is d  : False
# s1 is s2 : True
