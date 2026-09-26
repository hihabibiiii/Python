# Question 6 (Medium):
# Use all bitwise operators on integers a = 60 and b = 13.
# Print each result with a label.

# Solution:
a = 60   # Binary: 0011 1100
b = 13   # Binary: 0000 1101

print("a =", a, "(binary:", bin(a), ")")
print("b =", b, "(binary:", bin(b), ")")
print()
print("a & b  (AND)        =", a & b,  "->", bin(a & b))
print("a | b  (OR)         =", a | b,  "->", bin(a | b))
print("a ^ b  (XOR)        =", a ^ b,  "->", bin(a ^ b))
print("~a     (NOT)        =", ~a)
print("a << 2 (Left shift) =", a << 2, "->", bin(a << 2))
print("a >> 2 (Right shift)=", a >> 2, "->", bin(a >> 2))

# Output:
# a = 60 (binary: 0b111100 )
# b = 13 (binary: 0b1101 )
#
# a & b  (AND)        = 12 -> 0b1100
# a | b  (OR)         = 61 -> 0b111101
# a ^ b  (XOR)        = 49 -> 0b110001
# ~a     (NOT)        = -61
# a << 2 (Left shift) = 240 -> 0b11110000
# a >> 2 (Right shift)= 15 -> 0b1111
