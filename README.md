# Task Manager FastAPI

## Overview

This project converts a Python Task Manager application into a REST API using **FastAPI**.

The application provides CRUD operations for managing tasks. Task data is stored **in memory**, so the data will be lost when the application is restarted.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic
* Swagger UI

## Project Structure

```text
Task manager/
│
├── src/
│   ├── main.py
│   ├── task.py
│   └── task_manager.py
│
├── venv/
│
└── README.md
```

## Installation

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

## Running the Application

Start the FastAPI server using:

```bash
uvicorn src.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation is available at:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint           | Description             | Success Status |
| ------ | ------------------ | ----------------------- | -------------- |
| GET    | `/tasks`           | Get all tasks           | 200            |
| GET    | `/tasks/{task_id}` | Get a task by ID        | 200            |
| POST   | `/tasks`           | Create a new task       | 201            |
| PUT    | `/tasks/{task_id}` | Update an existing task | 200            |
| DELETE | `/tasks/{task_id}` | Delete a task           | 200            |

## Request Examples

### Create a Task

**POST `/tasks`**

Request body:

```json
{
  "title": "Learn FastAPI"
}
```

Response:

```json
{
  "task_id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

### Get All Tasks

**GET `/tasks`**

Response:

```json
[
  {
    "task_id": 1,
    "title": "Learn FastAPI",
    "completed": false
  }
]
```

### Get Task by ID

**GET `/tasks/1`**

Response:

```json
{
  "task_id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

### Update a Task

**PUT `/tasks/1`**

Request body:

```json
{
  "title": "Learn FastAPI deeply",
  "completed": true
}
```

Response:

```json
{
  "task_id": 1,
  "title": "Learn FastAPI deeply",
  "completed": true
}
```

### Delete a Task

**DELETE `/tasks/1`**

Response:

```json
{
  "message": "Task deleted successfully"
}
```

## Validation

The API uses **Pydantic models** to validate incoming JSON data.

For example, the task creation request requires a `title` field:

```json
{
  "title": "Learn FastAPI"
}
```

Invalid request data is automatically rejected by FastAPI.

## Error Handling

If a task ID does not exist, the API returns:

**HTTP 404 Not Found**

Example:

```json
{
  "detail": "Task not found"
}
```

## Testing

All endpoints were tested using the automatically generated **Swagger UI**.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

The following operations were tested successfully:

* Create a task
* Retrieve all tasks
* Retrieve a task by ID
* Update a task
* Delete a task
* Handle invalid task IDs

## Data Storage

The application currently uses an **in-memory list** to store tasks.

Therefore:

* No database is required.
* Data is available only while the application is running.
* Restarting the FastAPI server clears all tasks.

## Conclusion

This project demonstrates how a Python-based Task Manager can be converted into a REST API using FastAPI. It implements CRUD operations, request validation, JSON responses, HTTP status codes, error handling, and interactive API documentation using Swagger UI.
