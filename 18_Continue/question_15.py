# Question:
# You have a list of filenames.
# Use `continue` to skip files that do NOT have the ".py" extension.
# Print only the valid Python files.

# Example Output:
# Valid Python files:
# script.py
# main.py
# utils.py

filenames = [
    "script.py", "readme.txt", "main.py", "data.csv",
    "utils.py", "image.png", "test.py", "notes.docx"
]

print("Valid Python files:")
for fname in filenames:
    if not fname.endswith(".py"):
        continue
    print(fname)
