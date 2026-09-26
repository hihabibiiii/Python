# Question:
# Create a class Greeter where __init__ prints a message when an object is created.
# Show that the message appears automatically upon instantiation.

class Greeter:
    def __init__(self, name):
        self.name = name
        print(f"Greeter object created for: {name}")  # Printed in __init__

    def greet(self):
        print(f"Hello, {self.name}! Welcome!")

print("Creating objects...")
g1 = Greeter("Alice")
g2 = Greeter("Bob")
print("Objects created. Now calling greet():")
g1.greet()
g2.greet()
