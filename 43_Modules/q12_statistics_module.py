# Question: Import the statistics module and compute mean, median, and mode
# of a list of numbers. Also compute variance and standard deviation.

# Example output:
# Data: [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
# Mean:     5.2
# Median:   5.0
# Mode:     2 (appears most often)
# Variance: 5.511111...
# Std Dev:  2.347...

import statistics

# Dataset
data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
print(f"Data: {data}")
print(f"Sorted: {sorted(data)}")

print("\n--- Statistics Results ---")
print(f"Mean (average):       {statistics.mean(data)}")
print(f"Median (middle):      {statistics.median(data)}")
print(f"Mode (most frequent): {statistics.mode(data)}")
print(f"Variance:             {statistics.variance(data):.4f}")
print(f"Std Deviation:        {statistics.stdev(data):.4f}")

# User's own data
print("\n--- Compute Your Own ---")
raw = input("Enter numbers separated by spaces: ")
try:
    user_data = [float(x) for x in raw.split()]
    if len(user_data) < 2:
        print("Please enter at least 2 numbers.")
    else:
        print(f"Mean:   {statistics.mean(user_data):.2f}")
        print(f"Median: {statistics.median(user_data):.2f}")
        print(f"Std Dev: {statistics.stdev(user_data):.2f}")
except (ValueError, statistics.StatisticsError) as e:
    print(f"Error: {e}")
