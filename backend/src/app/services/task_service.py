from app.repositories.task_repository import TaskRepository
from app.models.task import Task

class TaskNotFoundError(Exception):
    pass

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def list_tasks(self) -> list[Task]:
        return self.repository.get_all()

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task {task_id} not found")
        return task

    def create_task(self, title: str) -> Task:
        return self.repository.create(title)

    def update_task(self, task_id: int, title: str, completed: bool) -> Task:
        task = self.repository.update(task_id, title, completed)
        if task is None:
            raise TaskNotFoundError(f"Task {task_id} not found")
        return task

    def delete_task(self, task_id: int) -> None:
        deleted = self.repository.delete(task_id)
        if not deleted:
            raise TaskNotFoundError(f"Task {task_id} not found")