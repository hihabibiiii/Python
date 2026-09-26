# Question:
# Print only odd numbers from 1 to 30 using `continue`.
# (Skip even numbers using continue.)

# Example Output:
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29

print("Odd numbers from 1 to 30:")
for i in range(1, 31):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
