# Question 6 (Medium):
# Define a function using *args to accept a variable number of positional arguments.
# Print all arguments and their count.

# Solution:
def print_all(*args):
    print(f"Number of arguments received: {len(args)}")
    for i, arg in enumerate(args, start=1):
        print(f"  Argument {i}: {arg}")

print("--- Calling with 3 arguments ---")
print_all("apple", "banana", "cherry")

print("\n--- Calling with 5 arguments ---")
print_all(10, 20, 30, 40, 50)

print("\n--- Calling with 1 argument ---")
print_all("only one")

print("\n--- Calling with no arguments ---")
print_all()

# Example Output:
# Number of arguments received: 3
#   Argument 1: apple
#   Argument 2: banana
#   Argument 3: cherry
