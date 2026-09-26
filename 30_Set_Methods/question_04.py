# Question:
# Create a set of numbers.
# Use pop() to remove and return an arbitrary element.
# Since sets are unordered, you cannot predict which element is removed.

numbers = {10, 20, 30, 40, 50}
print(f"Original set: {numbers}")

removed = numbers.pop()
print(f"Popped element: {removed}")
print(f"Set after pop: {numbers}")

removed2 = numbers.pop()
print(f"Popped element: {removed2}")
print(f"Set after second pop: {numbers}")
