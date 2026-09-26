# Question:
# Add numbers 1, 2, 3, ... to a running sum.
# Use break when the sum exceeds 100.
# Print the number that caused the sum to exceed 100 and the final sum.

# Example Output:
# Sum exceeded 100 at number 14. Total = 105

total = 0
for i in range(1, 1000):
    total += i
    if total > 100:
        print(f"Sum exceeded 100 at number {i}. Total = {total}")
        break
