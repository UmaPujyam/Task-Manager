from fastapi import APIRouter, HTTPException

from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import TaskService, TaskNotFoundError
from app.repositories.task_repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])

def get_task_service() -> TaskService:
    return TaskService(TaskRepository())

def to_response(task) -> TaskResponse:
    return TaskResponse(task_id=task.id, title=task.title, completed=task.completed)

@router.get("", response_model=list[TaskResponse])
def get_tasks():
    service = get_task_service()
    tasks = service.list_tasks()
    return [to_response(t) for t in tasks]

@router.post("", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    service = get_task_service()
    created = service.create_task(task.title)
    return to_response(created)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    service = get_task_service()
    try:
        task = service.get_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")
    return to_response(task)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate):
    service = get_task_service()
    try:
        task = service.update_task(task_id, task_data.title, task_data.completed)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")
    return to_response(task)

@router.delete("/{task_id}")
def delete_task(task_id: int):
    service = get_task_service()
    try:
        service.delete_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}