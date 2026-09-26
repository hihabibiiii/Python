# Question 7 (Medium):
# Take a price (float) from the user.
# Print the price formatted to exactly 2 decimal places using an f-string.

# Solution:
price = float(input("Enter the price: "))
print(f"The price is: ${price:.2f}")

# Example Input / Output:
# Enter the price: 9.5
# The price is: $9.50

# Enter the price: 19.999
# The price is: $20.00
