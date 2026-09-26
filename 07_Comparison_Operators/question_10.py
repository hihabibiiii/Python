# Question 10 (Medium):
# Take the prices of two products from the user.
# Compare them and print which product is cheaper (or if they cost the same).

# Solution:
product1 = input("Enter name of product 1: ")
price1 = float(input(f"Enter price of {product1}: $"))

product2 = input("Enter name of product 2: ")
price2 = float(input(f"Enter price of {product2}: $"))

if price1 < price2:
    print(f"{product1} (${price1}) is cheaper than {product2} (${price2}).")
elif price2 < price1:
    print(f"{product2} (${price2}) is cheaper than {product1} (${price1}).")
else:
    print(f"Both {product1} and {product2} cost the same: ${price1}.")

# Example:
# Coffee $2.5 vs Tea $1.8 -> Tea is cheaper
