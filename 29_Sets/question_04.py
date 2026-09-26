# Question:
# Create a set of colors.
# Use `in` to check if a color entered by the user is in the set.

# Example:
# Colors: {'red', 'blue', 'green', 'yellow'}
# Enter a color: green
# green is in the set!

colors = {"red", "blue", "green", "yellow"}
print(f"Colors: {colors}")

color = input("Enter a color to check: ").strip().lower()
if color in colors:
    print(f"{color} is in the set!")
else:
    print(f"{color} is NOT in the set.")
