# Question:
# Create a class ShoppingCart where __init__ initializes an empty list of items.
# Add a method to add items to the cart and display all items.

class ShoppingCart:
    def __init__(self):
        self.items = []  # Initialize empty list

    def add_item(self, item, price):
        self.items.append((item, price))

    def total(self):
        return sum(price for _, price in self.items)

    def display(self):
        print("Shopping Cart:")
        for item, price in self.items:
            print(f"  {item}: ${price:.2f}")
        print(f"  Total: ${self.total():.2f}")

cart = ShoppingCart()
cart.add_item("Apple", 0.99)
cart.add_item("Bread", 2.49)
cart.add_item("Milk", 1.79)
cart.display()
