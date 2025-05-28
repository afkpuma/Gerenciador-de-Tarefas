print("Hello, world!")
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task index.")

while True:
    print("\nChoose an action:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        try:
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(index)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '4':
        print("Exiting task manager.")
        break
    else:
        print("Invalid choice. Please try again.")
