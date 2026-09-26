# Question:
# Print numbers from 1 to 20.
# Use break to stop the loop when the number reaches 10.

# Example Output:
# 1 2 3 4 5 6 7 8 9 10
# Loop stopped at 10.

for i in range(1, 21):
    print(i, end=" ")
    if i == 10:
        break

print("\nLoop stopped at 10.")
