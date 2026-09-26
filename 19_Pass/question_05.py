# Question:
# Use `pass` to create a class body placeholder.
# Define a class Animal with pass in its body.
# Then create an instance of it.

# Note: This shows pass is valid inside a class definition.

class Animal:
    pass  # Class body will be filled in later

# Create an object of the empty class
dog = Animal()
print(f"Created an object: {dog}")
print(f"Type: {type(dog)}")
print("The class uses 'pass' as a placeholder for future code.")
