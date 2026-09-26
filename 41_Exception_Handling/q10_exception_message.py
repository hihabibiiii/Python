# Question: Use the 'as e' syntax to capture and print the actual exception message.
# Demonstrate this with multiple types of exceptions, printing the error type and message.

# Example outputs:
# Test 1 - ZeroDivisionError: division by zero
# Test 2 - ValueError: invalid literal for int() with base 10: 'abc'
# Test 3 - IndexError: list index out of range
# Test 4 - KeyError: 'missing_key'

# Test 1: ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Test 1 - {type(e).__name__}: {e}")

# Test 2: ValueError
try:
    num = int("abc")
except ValueError as e:
    print(f"Test 2 - {type(e).__name__}: {e}")

# Test 3: IndexError
try:
    my_list = [1, 2, 3]
    item = my_list[10]
except IndexError as e:
    print(f"Test 3 - {type(e).__name__}: {e}")

# Test 4: KeyError
try:
    my_dict = {"name": "Alice"}
    value = my_dict["missing_key"]
except KeyError as e:
    print(f"Test 4 - {type(e).__name__}: {e}")

print("\nAll tests completed! 'as e' gives us the actual error message.")
