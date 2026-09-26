# Question 11 (Hard):
# Print a simple table of student data using formatted print.
# The table should have columns: Name, Age, Score — aligned neatly.

# Solution:
# Header
print(f"{'Name':<12} {'Age':>4} {'Score':>6}")
print("-" * 24)

# Rows
print(f"{'Alice':<12} {20:>4} {88.5:>6.1f}")
print(f"{'Bob':<12} {22:>4} {74.0:>6.1f}")
print(f"{'Charlie':<12} {19:>4} {95.5:>6.1f}")

# Output:
# Name          Age  Score
# ------------------------
# Alice          20   88.5
# Bob            22   74.0
# Charlie        19   95.5
