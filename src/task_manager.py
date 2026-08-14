from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTasks:")
        for task in self.tasks:
            print(task)

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                print("Task marked as completed.")
                return

        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return

        print("Task not found.")