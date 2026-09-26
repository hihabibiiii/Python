# Question 5 (Easy):
# Define a function that takes name, age, and city as parameters.
# Call it using KEYWORD arguments (specify parameter names explicitly).
# Show that order doesn't matter when using keyword arguments.

# Solution:
def show_profile(name, age, city):
    print(f"Name: {name}")
    print(f"Age:  {age}")
    print(f"City: {city}")
    print()

# Positional call (order matters)
print("--- Positional call ---")
show_profile("Alice", 25, "Paris")

# Keyword call (order does NOT matter)
print("--- Keyword call ---")
show_profile(city="Berlin", name="Bob", age=32)

# Mixed: positional first, then keyword
print("--- Mixed call ---")
show_profile("Carol", city="Tokyo", age=28)

# Example Output:
# Name: Alice
# Age:  25
# City: Paris
#
# Name: Bob
# Age:  32
# City: Berlin
