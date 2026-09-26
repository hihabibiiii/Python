# Question:
# Loop through a list of strings.
# Use `pass` to skip empty strings (don't process them).
# Print only non-empty strings.

items = ["apple", "", "banana", "", "", "cherry", "date", ""]

print("Non-empty strings:")
for item in items:
    if item == "":
        pass  # Skip empty strings (placeholder; no action)
    else:
        print(f"  {item}")
