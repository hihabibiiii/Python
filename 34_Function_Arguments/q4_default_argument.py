# Question 4 (Easy):
# Define a function with a DEFAULT argument.
# The function should greet a person in a given language.
# Default language is "English". Call it with and without the language argument.

# Solution:
def greet(name, language="English"):
    if language == "English":
        msg = f"Hello, {name}!"
    elif language == "Spanish":
        msg = f"Hola, {name}!"
    elif language == "French":
        msg = f"Bonjour, {name}!"
    else:
        msg = f"Hi, {name}! (Language '{language}' not supported)"
    print(msg)

# Call without default argument
greet("Alice")

# Call with different languages
greet("Carlos", "Spanish")
greet("Marie", "French")
greet("Hana", "Japanese")

# Example Output:
# Hello, Alice!
# Hola, Carlos!
# Bonjour, Marie!
# Hi, Hana! (Language 'Japanese' not supported)
