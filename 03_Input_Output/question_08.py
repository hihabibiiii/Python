# Question 8 (Medium):
# Use str.format() to print a receipt showing:
#   Item name, quantity, and price.
# Format it neatly with aligned columns.

# Solution:
item = "Coffee"
quantity = 3
price = 2.50

print("===== Receipt =====")
print("Item     : {}".format(item))
print("Quantity : {}".format(quantity))
print("Price    : ${:.2f}".format(price))
print("Total    : ${:.2f}".format(quantity * price))
print("===================")

# Output:
# ===== Receipt =====
# Item     : Coffee
# Quantity : 3
# Price    : $2.50
# Total    : $7.50
# ===================
