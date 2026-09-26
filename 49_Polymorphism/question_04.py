# Question:
# Demonstrate polymorphism with the + operator.
# The same + operator behaves differently for int, str, and list.

# For integers: addition
a = 5 + 3
print(f"int + int:  5 + 3 = {a}")

# For strings: concatenation
b = "Hello" + " World"
print(f"str + str:  'Hello' + ' World' = '{b}'")

# For lists: merging
c = [1, 2] + [3, 4]
print(f"list + list:[1,2] + [3,4] = {c}")

# This is polymorphism: same operator, different behavior depending on type.
print("\nSame '+' operator behaves differently for int, str, and list.")
