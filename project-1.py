import json

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f'Task "{task}" added.')

    def update_task(self, index, task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = task
            self.save_tasks()
            print(f'Task {index + 1} updated to "{task}".')
        else:
            print("Invalid task number.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()
            print(f'Task {index + 1} marked as completed.')
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "✗"
            print(f"{index + 1}. [{status}] {task['task']}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Show Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.show_tasks()
            index = int(input("Enter task number to update: ")) - 1
            task = input("Enter the new task: ")
            todo_list.update_task(index, task)
        elif choice == '3':
            todo_list.show_tasks()
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            todo_list.show_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.show_tasks()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

