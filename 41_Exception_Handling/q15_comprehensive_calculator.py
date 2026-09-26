# Question: Create a comprehensive calculator with full exception handling.
# Support +, -, *, / operations. Handle ALL edge cases:
# - Non-numeric inputs (ValueError)
# - Division by zero (ZeroDivisionError)
# - Invalid operator (raise ValueError)
# - Unexpected errors (generic Exception)
# Use try/except/else/finally and a retry loop.

# Example:
# === Safe Calculator ===
# Enter first number: 10
# Enter operator (+, -, *, /): /
# Enter second number: 0
# Error: Cannot divide by zero!
# Closing calculator session.

# Enter first number: 10
# Enter operator (+, -, *, /): %
# Error: '%' is not a valid operator. Use +, -, *, /
# Closing calculator session.

def calculate(num1, operator, num2):
    """Perform calculation and raise appropriate exceptions."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2
    else:
        raise ValueError(f"'{operator}' is not a valid operator. Use +, -, *, /")

print("=" * 30)
print("   Comprehensive Safe Calculator")
print("=" * 30)

while True:
    print("\nEnter 'quit' to exit.\n")
    try:
        num1_input = input("Enter first number: ")
        if num1_input.lower() == 'quit':
            break
        num1 = float(num1_input)

        operator = input("Enter operator (+, -, *, /): ").strip()

        num2_input = input("Enter second number: ")
        if num2_input.lower() == 'quit':
            break
        num2 = float(num2_input)

        result = calculate(num1, operator, num2)

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        # Runs only if no exception occurred
        print(f"Result: {num1} {operator} {num2} = {result}")
    finally:
        # Always runs after each attempt
        print("Closing calculator session.")
