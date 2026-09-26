# Question:
# Print all numbers from 1 to 200 that are NOT divisible by 2, 3, or 5.
# Use `continue` to skip numbers divisible by 2, 3, or 5.

print("Numbers 1-200 not divisible by 2, 3, or 5:")
for i in range(1, 201):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    print(i, end=" ")
print()
