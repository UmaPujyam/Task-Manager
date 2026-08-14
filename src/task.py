class Task:
    def __init__(self, task_id, title):
        self.task_id = task_id
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.task_id}. {self.title} - {status}"