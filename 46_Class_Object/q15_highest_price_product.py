# Question: Create a class Product, create 5 objects, find the one with the highest price.

# Example output:
# Products:
# 1. Laptop    - $999.99
# 2. Phone     - $699.99
# 3. Tablet    - $499.99
# 4. Watch     - $299.99
# 5. Headphone - $149.99
# 
# Most expensive: Laptop at $999.99

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name:<12} - ${self.price:.2f} ({self.category})"

# Create 5 Product objects
products = [
    Product("Laptop",     999.99, "Electronics"),
    Product("Phone",      699.99, "Electronics"),
    Product("Tablet",     499.99, "Electronics"),
    Product("Watch",      299.99, "Accessories"),
    Product("Headphones", 149.99, "Audio"),
]

# Display all products
print("Products:")
for i, product in enumerate(products, 1):
    print(f"  {i}. {product}")

# Find the product with the highest price
most_expensive = max(products, key=lambda p: p.price)
print(f"\nMost expensive: {most_expensive.name} at ${most_expensive.price:.2f}")

# Find least expensive
least_expensive = min(products, key=lambda p: p.price)
print(f"Least expensive: {least_expensive.name} at ${least_expensive.price:.2f}")

# Sort by price descending
print("\nSorted by price (high to low):")
sorted_products = sorted(products, key=lambda p: p.price, reverse=True)
for i, p in enumerate(sorted_products, 1):
    print(f"  {i}. {p}")
