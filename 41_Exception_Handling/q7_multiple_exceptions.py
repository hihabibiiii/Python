# Question: Catch multiple exceptions in a SINGLE except clause using a tuple.
# Ask the user to enter a list index and a divisor.
# Catch both IndexError and ZeroDivisionError in one except block.

# Example:
# Numbers list: [10, 20, 30, 40, 50]
# Enter list index: 1
# Enter divisor: 0
# Error caught: division by zero

# Enter list index: 10
# Enter divisor: 2
# Error caught: list index out of range

numbers = [10, 20, 30, 40, 50]
print(f"Numbers list: {numbers}")

try:
    index = int(input("Enter list index: "))
    divisor = int(input("Enter divisor: "))
    value = numbers[index]
    result = value / divisor
    print(f"numbers[{index}] / {divisor} = {result}")
except (IndexError, ZeroDivisionError) as e:
    # Both exceptions are caught here in one clause
    print(f"Error caught: {e}")
except ValueError:
    print("Error: Please enter valid integers.")
