# Question:
# Use extended tuple unpacking to unpack a tuple.
# Given t = (1, 2, 3, 4, 5):
# Unpack into a=first, b=middle elements (list), c=last.
# Print a, b, c.

# Example Output:
# a = 1
# b = [2, 3, 4]
# c = 5

t = (1, 2, 3, 4, 5)
a, *b, c = t

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
