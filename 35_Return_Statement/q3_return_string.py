# Question 3 (Easy):
# Define a function called make_greeting that takes a name
# and returns a formatted greeting string.
# Assign the return value to a variable and print it.

# Solution:
def make_greeting(name):
    return f"Hello, {name}! Welcome aboard."

greeting1 = make_greeting("Alice")
greeting2 = make_greeting("Bob")

print(greeting1)
print(greeting2)

# Use return value directly in print
print(make_greeting("Carol"))

# Get name from user
name = input("\nEnter your name: ").strip()
message = make_greeting(name)
print(message)

# Example Input:  David
# Example Output: Hello, David! Welcome aboard.
