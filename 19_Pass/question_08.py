# Question:
# Loop through a list of tasks.
# For tasks marked as "TODO", use `pass` (no processing yet).
# For completed tasks, print them.

tasks = [
    ("Write report", "done"),
    ("Send email", "TODO"),
    ("Fix bug", "done"),
    ("Update database", "TODO"),
    ("Test app", "done")
]

print("Processing tasks:")
for task_name, status in tasks:
    if status == "TODO":
        pass  # Not implemented yet
    else:
        print(f"  [Done] {task_name}")

print("\nTODO tasks were skipped using pass (placeholder).")
