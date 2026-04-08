import json
import os

FILE_NAME = 'tasks.json'

def load_tasks():
    """Loads tasks from the JSON file if it exists."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task description: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks(tasks):
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks found. Enjoy your day!")
    for idx, task in enumerate(tasks):
        status = "[x]" if task['done'] else "[ ]"
        print(f"{idx + 1}. {status} {task['title']}")
    print("------------------\n")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['done'] = True
            save_tasks(tasks)
            print("🎉 Task marked as complete!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    print("Welcome to the Python Task Tracker!")
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
