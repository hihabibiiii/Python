# Question:
# Start with x = 60 (binary: 0b111100).
# Apply the following bitwise assignment operators one by one and print after each:
#   &= 45, |= 15, ^= 7
# Print the result and its binary representation.

x = 60
print(f"Initial: x = {x} (binary: {bin(x)})")

x &= 45
print(f"After &= 45: x = {x} (binary: {bin(x)})")

x |= 15
print(f"After |= 15: x = {x} (binary: {bin(x)})")

x ^= 7
print(f"After ^= 7: x = {x} (binary: {bin(x)})")
