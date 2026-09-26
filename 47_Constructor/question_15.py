# Question:
# Create a class Inventory where __init__ loads data from a hardcoded list.
# Populate instance attributes from that data.

class Inventory:
    # Class-level "database"
    _catalog = [
        {"id": 1, "name": "Laptop",  "price": 999.99, "stock": 10},
        {"id": 2, "name": "Mouse",   "price":  29.99, "stock": 50},
        {"id": 3, "name": "Keyboard","price":  79.99, "stock": 30},
        {"id": 4, "name": "Monitor", "price": 399.99, "stock": 15},
    ]

    def __init__(self):
        # Load data from catalog into instance
        self.items = []
        for item in Inventory._catalog:
            self.items.append(dict(item))  # Copy each item
        print(f"Inventory loaded with {len(self.items)} items.")

    def display(self):
        print(f"{'ID':<5} {'Name':<12} {'Price':>10} {'Stock':>8}")
        print("-" * 40)
        for item in self.items:
            print(f"{item['id']:<5} {item['name']:<12} "
                  f"${item['price']:>9.2f} {item['stock']:>8}")

    def total_value(self):
        return sum(i["price"] * i["stock"] for i in self.items)

inv = Inventory()
inv.display()
print(f"\nTotal inventory value: ${inv.total_value():,.2f}")
