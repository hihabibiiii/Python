# Question:
# Print numbers from 1 to 50.
# Skip any number that is divisible by 5 using `continue`.

print("Numbers 1 to 50 (skipping multiples of 5):")
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i, end=" ")
print()
