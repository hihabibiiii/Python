# Question: Implement a stack using a list.
# Push 5 items onto the stack, pop 3 items off, and print the remaining stack.
# Stack: LIFO (Last In, First Out)
# push = append(), pop = pop()

stack = []
print("=== Stack Demo (LIFO) ===")

# Push 5 items
items_to_push = [10, 20, 30, 40, 50]
for item in items_to_push:
    stack.append(item)
    print(f"Pushed: {item} | Stack: {stack}")

print()

# Pop 3 items
print("Popping 3 items:")
for i in range(3):
    popped = stack.pop()
    print(f"Popped: {popped} | Stack: {stack}")

print()
print("Remaining stack:", stack)
