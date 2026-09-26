# Question: Read a CSV-style text file (comma-separated values) and display
# the data as a formatted table. First write the CSV data, then parse and display it.

# Example output:
# CSV file created.
# 
# Displaying as formatted table:
# +-----------+-----+---------+
# | Name      | Age | City    |
# +-----------+-----+---------+
# | Alice     | 30  | London  |
# | Bob       | 25  | Paris   |
# | Charlie   | 35  | Tokyo   |
# | Diana     | 28  | Berlin  |
# +-----------+-----+---------+

# Step 1: Create a CSV-style text file manually
csv_data = """Name,Age,City
Alice,30,London
Bob,25,Paris
Charlie,35,Tokyo
Diana,28,Berlin"""

with open('people.csv', 'w') as f:
    f.write(csv_data)

print("CSV file created.")

# Step 2: Parse and display as a formatted table
with open('people.csv', 'r') as f:
    lines = f.readlines()

# Parse each row
rows = []
for line in lines:
    row = [col.strip() for col in line.strip().split(',')]
    rows.append(row)

# Calculate column widths
headers = rows[0]
data_rows = rows[1:]
col_widths = [max(len(headers[i]), max(len(r[i]) for r in data_rows)) for i in range(len(headers))]

# Build separator
sep = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

# Print table
print("\nDisplaying as formatted table:")
print(sep)
# Header
print("|" + "|".join(f" {headers[i]:<{col_widths[i]}} " for i in range(len(headers))) + "|")
print(sep)
# Data rows
for row in data_rows:
    print("|" + "|".join(f" {row[i]:<{col_widths[i]}} " for i in range(len(row))) + "|")
print(sep)
