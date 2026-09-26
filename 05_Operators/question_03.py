# Question 3 (Easy):
# Demonstrate logical operators: and, or, not.
# Use two boolean conditions and print all combinations.

# Solution:
p = True
q = False

print("p =", p, ", q =", q)
print("p and q :", p and q)   # Both must be True
print("p or  q :", p or q)    # At least one must be True
print("not p   :", not p)     # Reverses the boolean
print("not q   :", not q)

# Practical example with numbers:
a = 8
print("\na =", a)
print("a > 5 and a < 15 :", a > 5 and a < 15)   # True
print("a < 3 or  a > 7  :", a < 3 or a > 7)     # True
print("not (a == 8)     :", not (a == 8))        # False

# Output:
# p = True , q = False
# p and q : False
# p or  q : True
# not p   : False
# not q   : True
#
# a = 8
# a > 5 and a < 15 : True
# a < 3 or  a > 7  : True
# not (a == 8)     : False
