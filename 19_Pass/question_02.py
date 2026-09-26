# Question:
# Use `pass` inside a for loop body.
# The loop iterates but the body does nothing.
# This is useful as a placeholder while planning code.

# Example:
# Looping over [1, 2, 3, 4, 5] with pass body.

numbers = [1, 2, 3, 4, 5]

print("Starting loop (with pass body)...")
for num in numbers:
    pass  # Placeholder: processing logic will go here

print("Loop finished. (No output from body because pass was used.)")
print(f"Last value of num after loop: {num}")
