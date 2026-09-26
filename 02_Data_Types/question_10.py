# Question 10 (Medium):
# Use sys.getsizeof() to find the memory size (in bytes) of different data types.
# Check: int, float, str, and list.
# Print the type and its size.

# Solution:
import sys

integer_val = 42
float_val = 3.14
string_val = "hello"
list_val = [1, 2, 3]

print("int   size:", sys.getsizeof(integer_val), "bytes")
print("float size:", sys.getsizeof(float_val), "bytes")
print("str   size:", sys.getsizeof(string_val), "bytes")
print("list  size:", sys.getsizeof(list_val), "bytes")

# Output (may vary slightly by platform/Python version):
# int   size: 28 bytes
# float size: 24 bytes
# str   size: 54 bytes
# list  size: 88 bytes
