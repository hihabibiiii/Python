# Question:
# Create a function stub using `pass`.
# Define a function calculate_tax() that does nothing yet (pass body).
# Call it to show it runs without error.

def calculate_tax(income):
    pass  # TODO: implement tax calculation logic

def generate_report(data):
    pass  # TODO: implement report generation

# Call the stub functions
result = calculate_tax(50000)
print(f"calculate_tax(50000) returned: {result}")  # Returns None

generate_report([])
print("generate_report() called successfully.")
print("Both functions use 'pass' as stubs.")
