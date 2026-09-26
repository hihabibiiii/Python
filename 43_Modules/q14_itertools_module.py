# Question: Use the itertools module: chain(), combinations(), and permutations().
# Demonstrate each function with practical examples.

# Example output:
# chain(['a','b'], [1,2,3]): ['a', 'b', 1, 2, 3]
# combinations([1,2,3,4], 2): [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
# permutations('ABC', 2): [('A','B'),('A','C'),('B','A'),('B','C'),('C','A'),('C','B')]

import itertools

print("=" * 50)
print("         itertools Module Demo")
print("=" * 50)

# chain: combine multiple iterables into one
print("\n--- itertools.chain() ---")
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combined = list(itertools.chain(letters, numbers))
print(f"chain({letters}, {numbers}):")
print(f"  Result: {combined}")

# combinations: choose r items from iterable (order doesn't matter)
print("\n--- itertools.combinations() ---")
items = [1, 2, 3, 4]
combos = list(itertools.combinations(items, 2))
print(f"combinations({items}, 2):")
print(f"  Result: {combos}")
print(f"  Total: {len(combos)} combinations")

# permutations: arrange r items from iterable (order matters)
print("\n--- itertools.permutations() ---")
chars = 'ABC'
perms = list(itertools.permutations(chars, 2))
print(f"permutations('{chars}', 2):")
print(f"  Result: {perms}")
print(f"  Total: {len(perms)} permutations")

# product: Cartesian product
print("\n--- itertools.product() ---")
colors = ['Red', 'Blue']
sizes = ['S', 'M', 'L']
products = list(itertools.product(colors, sizes))
print(f"product({colors}, {sizes}):")
for p in products:
    print(f"  {p}")
