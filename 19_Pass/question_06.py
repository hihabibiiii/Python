# Question:
# Use `pass` inside a try/except block.
# Intentionally ignore a specific error (divide by zero).
# This demonstrates silencing an error using pass.

# Note: In real code, silently ignoring errors is usually bad practice.
# This is only for demonstration purposes.

numbers = [10, 5, 0, 2]

for num in numbers:
    try:
        result = 100 / num
        print(f"100 / {num} = {result:.2f}")
    except ZeroDivisionError:
        pass  # Intentionally ignoring division by zero

print("Done. Zero division errors were silently ignored using pass.")
