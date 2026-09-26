# Question 7 (Medium):
# Use the 'global' keyword to create a counter that increments
# each time a function is called. Demonstrate persistent state via global.

# Solution:
call_count = 0   # global counter

def do_task(task_name):
    global call_count
    call_count += 1
    print(f"[Call #{call_count}] Running task: '{task_name}'")

do_task("Load data")
do_task("Process data")
do_task("Save results")
do_task("Send report")

print(f"\nTotal tasks completed: {call_count}")

# Example Output:
# [Call #1] Running task: 'Load data'
# [Call #2] Running task: 'Process data'
# [Call #3] Running task: 'Save results'
# [Call #4] Running task: 'Send report'
# Total tasks completed: 4
