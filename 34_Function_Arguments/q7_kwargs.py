# Question 7 (Medium):
# Define a function using **kwargs to accept any number of keyword arguments.
# Print all keyword-value pairs.

# Solution:
def print_info(**kwargs):
    print(f"Received {len(kwargs)} keyword argument(s):")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("--- Person info ---")
print_info(name="Alice", age=25, city="Rome")

print("\n--- Server config ---")
print_info(host="localhost", port=8080, debug=True, timeout=30)

print("\n--- Empty call ---")
print_info()

# Example Output:
# --- Person info ---
# Received 3 keyword argument(s):
#   name: Alice
#   age: 25
#   city: Rome
