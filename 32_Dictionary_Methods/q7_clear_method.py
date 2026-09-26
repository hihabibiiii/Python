# Question 7 (Medium):
# Create a dictionary with several key-value pairs.
# Use the clear() method to remove all items.
# Print the dictionary before and after clearing.

# Solution:
shopping_cart = {
    "milk": 2,
    "bread": 1,
    "eggs": 12,
    "butter": 1,
    "cheese": 3
}

print("Shopping cart before clear():")
for item, qty in shopping_cart.items():
    print(f"  {item}: {qty}")

shopping_cart.clear()

print("\nShopping cart after clear():", shopping_cart)
print("Length after clear():", len(shopping_cart))

# Note: clear() is different from del or reassigning
another_dict = {"a": 1, "b": 2}
reference = another_dict      # both point to same dict
another_dict.clear()
print("\nUsing clear() also empties the reference:", reference)

# Example Output:
# Shopping cart before clear():
#   milk: 2
#   bread: 1
#   eggs: 12
#   butter: 1
#   cheese: 3
# Shopping cart after clear(): {}
# Length after clear(): 0
