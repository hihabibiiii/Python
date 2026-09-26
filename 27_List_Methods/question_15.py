# Question:
# Implement a Queue (FIFO) using a list.
# Enqueue 5 items using append(), then dequeue 3 using pop(0).
# Print the queue state after each operation.

# FIFO: First In, First Out

queue = []
print("=== Queue Simulation (FIFO) ===")

# Enqueue 5 items
items_to_add = ["Task A", "Task B", "Task C", "Task D", "Task E"]
for item in items_to_add:
    queue.append(item)
    print(f"Enqueued: '{item}' -> Queue: {queue}")

print()

# Dequeue 3 items
for _ in range(3):
    removed = queue.pop(0)
    print(f"Dequeued: '{removed}' -> Queue: {queue}")

print(f"\nFinal queue: {queue}")
