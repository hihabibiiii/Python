# Question:
# Use a combination of append(), remove(), and sort() to simulate a priority queue.
# Add tasks with priorities, sort by priority, then process (remove) the highest priority.

# Lower number = higher priority.

tasks = []
tasks.append((1, "Fix critical bug"))
tasks.append((3, "Write documentation"))
tasks.append((2, "Code review"))
tasks.append((1, "Deploy hotfix"))
tasks.append((4, "Update README"))

print("Tasks added:")
for t in tasks:
    print(f"  Priority {t[0]}: {t[1]}")

# Sort by priority
tasks.sort(key=lambda x: x[0])

print("\nProcessing tasks in priority order:")
while tasks:
    task = tasks.pop(0)  # Remove highest priority (front)
    print(f"  Processing [{task[0]}]: {task[1]}")
