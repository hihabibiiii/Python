# Question:
# Print numbers from 1 to 100.
# Skip perfect squares (1, 4, 9, 16, 25, ...) using `continue`.

print("Numbers 1-100 (skipping perfect squares):")
for i in range(1, 101):
    if int(i**0.5)**2 == i:
        continue
    print(i, end=" ")
print()
