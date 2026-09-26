# Question: Compute the time elapsed for a block of code using datetime.
# Simulate a task and measure how long it takes to run.

# Example output:
# === Code Timing Demo ===
# Starting task...
# Task completed!
# Time elapsed: 0.002345 seconds
# (or: 0 minutes, 0.002 seconds)

import datetime
import time

print("=" * 35)
print("       Code Timing Demo")
print("=" * 35)

# Method 1: Using datetime.datetime.now()
print("\nMethod 1: Using datetime.datetime.now()")
start_time = datetime.datetime.now()

# --- Code to time starts here ---
print("Simulating a task (counting to 1,000,000)...")
total = sum(range(1_000_001))
print(f"Sum computed: {total:,}")
# --- Code to time ends here ---

end_time = datetime.datetime.now()
elapsed = end_time - start_time  # Returns a timedelta object

print(f"\nStart time: {start_time.strftime('%H:%M:%S.%f')}")
print(f"End time:   {end_time.strftime('%H:%M:%S.%f')}")
print(f"Elapsed:    {elapsed.total_seconds():.6f} seconds")

# Method 2: Using time.time() for benchmarking
print("\nMethod 2: Using time.time() (simpler for benchmarks)")
t1 = time.time()
result = [x**2 for x in range(100_000)]
t2 = time.time()
print(f"List comprehension of 100k squares took: {t2 - t1:.6f} seconds")
