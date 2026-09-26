# Question 6 (Medium):
# Ask the user to enter a key name.
# Check if that key exists in a predefined dictionary using the 'in' keyword.
# Print an appropriate message.

# Solution:
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 20,
    "grapes": 15
}

key = input("Enter a key to check (e.g. apples, bananas): ").strip()

if key in inventory:
    print(f"'{key}' exists in the dictionary with value: {inventory[key]}")
else:
    print(f"'{key}' does NOT exist in the dictionary.")

# Example Input:  apples
# Example Output: 'apples' exists in the dictionary with value: 50

# Example Input:  mango
# Example Output: 'mango' does NOT exist in the dictionary.
