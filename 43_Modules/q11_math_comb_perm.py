# Question: Use math.comb() and math.perm() to compute combinations and permutations.
# Demonstrate with lottery examples and let the user compute their own.

# Combinations C(n,r): choosing r items from n WITHOUT regard to order.
# Permutations P(n,r): arranging r items from n WITH regard to order.

# Example output:
# Lottery: Choose 6 from 49 numbers
# Combinations C(49, 6) = 13983816
# Ways to arrange 3 winners from 49: Permutations P(49, 3) = 107880

import math

print("=" * 45)
print("   Combinations & Permutations Demo")
print("=" * 45)

# Combinations
print("\n--- Combinations C(n, r) ---")
print("(Order does NOT matter)")
print(f"C(5, 2) = {math.comb(5, 2)}    (choose 2 from 5)")
print(f"C(10, 3) = {math.comb(10, 3)}   (choose 3 from 10)")
print(f"Lottery C(49, 6) = {math.comb(49, 6)}")

# Permutations
print("\n--- Permutations P(n, r) ---")
print("(Order DOES matter)")
print(f"P(5, 2) = {math.perm(5, 2)}    (arrange 2 from 5)")
print(f"P(10, 3) = {math.perm(10, 3)}  (arrange 3 from 10)")
print(f"P(49, 3) = {math.perm(49, 3)}")

# User input
print()
n = int(input("Enter n (total items): "))
r = int(input("Enter r (items to choose/arrange): "))

if r > n:
    print("Error: r cannot be greater than n!")
else:
    print(f"\nC({n}, {r}) = {math.comb(n, r)}  (combinations)")
    print(f"P({n}, {r}) = {math.perm(n, r)}  (permutations)")
