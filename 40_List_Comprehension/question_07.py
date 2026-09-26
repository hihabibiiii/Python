# Question:
# Create all pairs (i, j) where i != j, for i in range(4) and j in range(4).
# Use nested list comprehension.

pairs = [(i, j) for i in range(4) for j in range(4) if i != j]
print("Pairs where i != j:")
for pair in pairs:
    print(f"  {pair}")
print(f"Total pairs: {len(pairs)}")
