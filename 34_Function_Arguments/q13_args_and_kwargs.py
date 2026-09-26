# Question 13 (Hard):
# Write a function that accepts both *args and **kwargs.
# Categorise and display the two groups separately.

# Solution:
def categorize(*args, **kwargs):
    print("Positional arguments (*args):")
    if args:
        for i, val in enumerate(args, 1):
            print(f"  [{i}] {val} (type: {type(val).__name__})")
    else:
        print("  None")

    print("\nKeyword arguments (**kwargs):")
    if kwargs:
        for key, val in kwargs.items():
            print(f"  {key} = {val} (type: {type(val).__name__})")
    else:
        print("  None")
    print()

# Test with various inputs
categorize(1, 2, 3)
categorize(name="Alice", age=25)
categorize("hello", True, 42, city="Cairo", score=95.5)
categorize()

# Example Output:
# Positional arguments (*args):
#   [1] hello (type: str)
#   [2] True (type: bool)
#   [3] 42 (type: int)
# Keyword arguments (**kwargs):
#   city = Cairo (type: str)
#   score = 95.5 (type: float)
