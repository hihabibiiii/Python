# Question:
# Loop through a list of fruits.
# Skip items that start with the letter "B" using `continue`.
# Print all other items.

# Example Output:
# apple
# cherry
# date
# elderberry

fruits = ["apple", "banana", "cherry", "blueberry", "date", "elderberry"]
skip_letter = "B"
print(f"Fruits (skipping those starting with '{skip_letter}'):")

for fruit in fruits:
    if fruit.upper().startswith(skip_letter):
        continue
    print(fruit)
