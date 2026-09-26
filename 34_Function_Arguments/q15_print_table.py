# Question 15 (Hard):
# Write a flexible print_table() function that:
#   - Accepts *args as rows (each row is a tuple/list of values)
#   - Accepts **kwargs for column widths (e.g. col1=10, col2=15, col3=8)
# Print a nicely formatted table.

# Solution:
def print_table(*args, **kwargs):
    # Get column widths from kwargs; default width is 12
    col_widths = list(kwargs.values()) if kwargs else []

    # Determine number of columns from first row
    if not args:
        print("No rows to display.")
        return

    num_cols = len(args[0])

    # Fill missing widths with default of 12
    while len(col_widths) < num_cols:
        col_widths.append(12)

    # Print separator line
    sep = "+" + "+".join("-" * (w + 2) for w in col_widths[:num_cols]) + "+"

    print(sep)
    for row in args:
        cells = []
        for i, cell in enumerate(row):
            w = col_widths[i] if i < len(col_widths) else 12
            cells.append(f" {str(cell):<{w}} ")
        print("|" + "|".join(cells) + "|")
        print(sep)

# Call with column width kwargs and row tuples as args
print_table(
    ("Name",    "Score", "Grade"),
    ("Alice",   95,      "A"),
    ("Bob",     72,      "B"),
    ("Carol",   88,      "A-"),
    col1=10, col2=7, col3=6
)

# Example Output:
# +------------+---------+--------+
# | Name       | Score   | Grade  |
# +------------+---------+--------+
# | Alice      | 95      | A      |
# +------------+---------+--------+
# ...
