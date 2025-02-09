# task_manager.py

# Step 1: Set Up the Project
class Task:
    def __init__(self, name, due_date=None):
        self.name = name
        self.due_date = due_date

    def __str__(self):
        return f"{self.name} (Due: {self.due_date})"

tasks = []  # List to store tasks

# Step 2: Implement Core Functions

def add_task(name, due_date=None):
    """Add a new task to the list."""
    task = Task(name, due_date)
    tasks.append(task)
    print(f"Task added: {task}")
    save_tasks()


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

def save_tasks():
   try:
    with open('tasks.txt',"w") as file:
       for task in tasks:
        file.write(f'{task.name}, {task.due_date}/n')
    print("Tasks saved successfully.")
   except Exception as e:
        print(f"Error saving tasks:{e}")

def load_tasks():
    try:
        with open('tasks.txt','r') as file:
            for line in file:
                name,due_date = line.strip().split(',')
                tasks.append(Task(name,due_date if due_date else None))
        print("Tasks loaded successfully.")

    except FileNotFoundError:
        print("No saved tasks found")
    except Exception as e:
        print(f"Error loading tasks: {e}")


# Step 3: Create the Main Menu

def main_menu():
    while True:
        print("\n---Task Manager ---")
        print("1. Add Task")
        print("2. List Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter task name: ")
            due_date = input("Enter due date (optional):")
            add_task(name,due_date if due_date else None)

        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task Id to delete: "))
            delete_task(task_id)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")   

    if __name__ == "__main__":
        load_tasks()
        main_menu()
        save_tasks() 
