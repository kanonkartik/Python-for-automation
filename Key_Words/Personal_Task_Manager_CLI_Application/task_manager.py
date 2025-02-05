# task_manager.py

class Task:
    def __init__(self, name, due_date=None):
        self.name = name
        self.due_date = due_date

    def __str__(self):
        return f"{self.name} (Due: {self.due_date})"

tasks = []  # List to store tasks

def add_task(name, due_date=None):
    """Add a new task to the list."""
    task = Task(name, due_date)
    tasks.append(task)
    print(f"Task added: {task}")

def list_tasks():
    """List all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(task_id):
    """here we delete the task"""
    try:
        task = task.pop(task_id - 1)
        print(f"Deleted task: {task}")
    except IndexError:
        print("Invalid task ID.")
