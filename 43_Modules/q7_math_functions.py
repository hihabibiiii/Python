# Question: Use math module functions: floor(), ceil(), log(), and sin().
# Demonstrate each function with examples and user input.

# Example output:
# === Math Module Functions ===
# math.floor(4.7) = 4        (round DOWN)
# math.ceil(4.2)  = 5        (round UP)
# math.log(100, 10) = 2.0    (log base 10 of 100)
# math.sin(0) = 0.0
# math.sin(pi/2) = 1.0
# math.cos(0) = 1.0

import math

print("=" * 40)
print("       Math Module Functions")
print("=" * 40)

# floor and ceil
print(f"\nmath.floor(4.7) = {math.floor(4.7)}  (round DOWN)")
print(f"math.floor(-4.3) = {math.floor(-4.3)}  (floor of negative)")
print(f"math.ceil(4.2)  = {math.ceil(4.2)}   (round UP)")
print(f"math.ceil(-4.7) = {math.ceil(-4.7)}  (ceil of negative)")

# log
print(f"\nmath.log(100, 10) = {math.log(100, 10)}  (log base 10 of 100)")
print(f"math.log(math.e)  = {math.log(math.e)}   (natural log of e)")
print(f"math.log2(8)      = {math.log2(8)}      (log base 2 of 8)")

# trig
print(f"\nmath.sin(0)        = {math.sin(0)}")
print(f"math.sin(pi/2)     = {math.sin(math.pi/2)}")
print(f"math.cos(0)        = {math.cos(0)}")
print(f"math.tan(pi/4)     = {math.tan(math.pi/4):.6f}")

# User input
num = float(input("\nEnter a number to compute floor, ceil, and sqrt: "))
print(f"floor({num}) = {math.floor(num)}")
print(f"ceil({num})  = {math.ceil(num)}")
if num >= 0:
    print(f"sqrt({num})  = {math.sqrt(num)}")
