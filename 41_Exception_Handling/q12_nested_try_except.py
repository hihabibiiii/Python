# Question: Demonstrate nested try/except blocks.
# Outer try: get an integer index from the user (catch ValueError).
# Inner try: use that index to access a list (catch IndexError).
# Show how inner and outer exceptions are handled separately.

# Example:
# Items: ['laptop', 'phone', 'tablet', 'camera']
# Enter an index: abc
# Outer error: 'abc' is not a valid integer!

# Enter an index: 10
# Inner error: Index 10 is out of range for this list!

# Enter an index: 2
# Item at index 2: tablet

items = ['laptop', 'phone', 'tablet', 'camera']
print(f"Items: {items}")

try:
    # Outer try: handle non-integer input
    index = int(input("Enter an index: "))
    
    try:
        # Inner try: handle out-of-range index
        item = items[index]
        print(f"Item at index {index}: {item}")
    except IndexError:
        print(f"Inner error: Index {index} is out of range for this list!")

except ValueError:
    print(f"Outer error: That is not a valid integer!")
