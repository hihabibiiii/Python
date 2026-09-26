# Question:
# Demonstrate the __del__ destructor.
# It is called when an object is deleted or goes out of scope.
# Print a message in __del__.

class Connection:
    def __init__(self, host):
        self.host = host
        print(f"Connection opened to: {host}")

    def __del__(self):
        print(f"Connection to {self.host} closed.  (__del__ called)")

print("Creating connection...")
conn = Connection("database.example.com")
print("Using connection...")
print("Deleting connection manually...")
del conn
print("After del - destructor was called above.")
