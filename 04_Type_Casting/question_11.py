# Question 11 (Hard):
# Convert a hex string '0xFF' to an integer using int() with base 16.
# Convert a binary string '0b1010' to an integer using int() with base 2.
# Print each result.

# Solution:
hex_string = '0xFF'
hex_to_int = int(hex_string, 16)
print(f"Hex '{hex_string}' -> int: {hex_to_int}")

binary_string = '0b1010'
# int() with base 2 does not handle '0b' prefix directly, strip it:
binary_to_int = int(binary_string, 2)
print(f"Binary '{binary_string}' -> int: {binary_to_int}")

# Also using int() with the prefix automatically handled by base 0:
hex_auto = int('0xFF', 0)
bin_auto = int('0b1010', 0)
print(f"\nUsing base=0 (auto-detect):")
print(f"'0xFF'   -> {hex_auto}")
print(f"'0b1010' -> {bin_auto}")

# Output:
# Hex '0xFF' -> int: 255
# Binary '0b1010' -> int: 10
#
# Using base=0 (auto-detect):
# '0xFF'   -> 255
# '0b1010' -> 10
