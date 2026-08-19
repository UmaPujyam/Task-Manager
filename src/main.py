from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.task import Task

app = FastAPI()


# Request model for creating a task
class TaskCreate(BaseModel):
    title: str


# Request model for updating a task
class TaskUpdate(BaseModel):
    title: str
    completed: bool


# Response model
class TaskResponse(BaseModel):
    task_id: int
    title: str
    completed: bool


# In-memory storage
tasks = []
next_id = 1


# GET all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks


# POST create a new task
@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    global next_id

    new_task = Task(next_id, task.title)
    tasks.append(new_task)
    next_id += 1

    return new_task


# GET a single task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task.task_id == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# PUT update a task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate):
    for task in tasks:
        if task.task_id == task_id:
            task.title = task_data.title
            task.completed = task_data.completed
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# DELETE a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )