class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty.")

# Example usage
if __name__ == "__main__":
    todo = ToDoList()
    todo.display_tasks()

    todo.add_task("Finish homework")
    todo.add_task("Buy groceries")
    todo.add_task("Call mom")

    todo.display_tasks()

    todo.remove_task("Buy groceries")


    todo.display_tasks()
