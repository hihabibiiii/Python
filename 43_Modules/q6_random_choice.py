# Question: Use random.choice() to pick a random item from a list.
# Create a list of colors, fruits, and motivational quotes.
# Use random.choice() to pick one from each list.

# Example output:
# === Random Picker ===
# Random color: Blue
# Random fruit: Mango
# Today's motivation: "Keep going, you're doing great!"

import random

colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink"]
fruits = ["Apple", "Mango", "Banana", "Strawberry", "Grapes", "Pineapple"]
quotes = [
    "Keep going, you're doing great!",
    "Every expert was once a beginner.",
    "Small steps lead to big achievements.",
    "Consistency is the key to success.",
    "Believe in yourself!"
]

print("=" * 30)
print("       Random Picker")
print("=" * 30)

random_color = random.choice(colors)
random_fruit = random.choice(fruits)
random_quote = random.choice(quotes)

print(f"Random color: {random_color}")
print(f"Random fruit: {random_fruit}")
print(f"Today's motivation: \"{random_quote}\"")

print()
# Let user pick a category
category = input("Pick a category (colors/fruits/quotes): ").lower()
if category == "colors":
    print(f"Your random color: {random.choice(colors)}")
elif category == "fruits":
    print(f"Your random fruit: {random.choice(fruits)}")
elif category == "quotes":
    print(f"Your quote: \"{random.choice(quotes)}\"")
else:
    print("Unknown category!")
