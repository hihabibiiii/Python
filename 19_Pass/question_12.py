# Question:
# Use `pass` inside a while loop that checks a condition
# but delegates the work to an external counter.
# The loop body is a pass; the counter increments in the condition.

# This simulates a "busy-wait" style loop.

print("Counting to 5 using a while loop with pass body:")

count = 0
while (count := count + 1) <= 5:
    pass  # All logic is in the while condition itself

print(f"Loop ended. count = {count}")
