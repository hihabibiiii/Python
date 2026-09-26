# Question: Create a class TodoList with tasks list and methods:
# add_task(), remove_task(), show_tasks(), mark_done().

# Example output:
# === My Todo List ===
# Task added: 'Buy groceries'
# Task added: 'Study Python'
# Task added: 'Go for a run'
# 
# --- Tasks ---
# [ ] 1. Buy groceries
# [ ] 2. Study Python
# [ ] 3. Go for a run
# 
# Marked 'Study Python' as done!
# [ ] 1. Buy groceries
# [✓] 2. Study Python
# [ ] 3. Go for a run

class TodoList:
    def __init__(self, title="My Todo List"):
        self.title = title
        self.tasks = []   # Each item: {'name': ..., 'done': False}

    def add_task(self, task_name):
        self.tasks.append({'name': task_name, 'done': False})
        print(f"Task added: '{task_name}'")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task['name'] == task_name:
                self.tasks.remove(task)
                print(f"Task removed: '{task_name}'")
                return
        print(f"Task '{task_name}' not found.")

    def mark_done(self, task_name):
        for task in self.tasks:
            if task['name'] == task_name:
                task['done'] = True
                print(f"Marked '{task_name}' as done!")
                return
        print(f"Task '{task_name}' not found.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in list!")
            return
        print(f"\n--- {self.title} ---")
        for i, task in enumerate(self.tasks, 1):
            status = "[✓]" if task['done'] else "[ ]"
            print(f"  {status} {i}. {task['name']}")
        done_count = sum(1 for t in self.tasks if t['done'])
        print(f"  Progress: {done_count}/{len(self.tasks)} done")

# Test the TodoList
todo = TodoList("Daily Tasks")
print(f"=== {todo.title} ===")

todo.add_task("Buy groceries")
todo.add_task("Study Python")
todo.add_task("Go for a run")
todo.add_task("Call mom")

todo.show_tasks()

todo.mark_done("Study Python")
todo.mark_done("Go for a run")
todo.show_tasks()

todo.remove_task("Buy groceries")
todo.show_tasks()
