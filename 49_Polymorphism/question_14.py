# Question:
# Override both __repr__ and __str__ and demonstrate the difference.
# __str__: human-readable, used by print() and str()
# __repr__: developer-friendly, used in repr() and the REPL

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

p = Product("Laptop", 999.99)

print("print(p) uses __str__:")
print(p)

print("\nrepr(p) uses __repr__:")
print(repr(p))

print("\nIn a list, repr() is used:")
products = [Product("Mouse", 29.99), Product("Keyboard", 79.99)]
print(products)  # Each element shows __repr__
