<<<<<<< HEAD
# Task Manager — React Frontend

A React frontend for managing tasks, built with **Vite**. This version uses **mock/sample data** and is **not yet connected** to a backend API (FastAPI integration is a planned future step).

---

## Features

- Display list of tasks
- Add a new task
- Mark a task as completed
- Delete a task
- Empty state UI shown when there are no tasks

---

## Component Structure

```
App
├── TaskForm    → controlled form to add new tasks
└── TaskList    → renders task list or empty state
     └── TaskItem → displays one task, handles toggle/delete
```

- **App.jsx** — owns the task state (array of tasks) and defines the logic for adding, toggling, and deleting tasks. Passes data and functions down as props.
- **TaskForm.jsx** — a controlled form component that captures new task input and calls `onAddTask` when submitted.
- **TaskList.jsx** — renders the list of tasks by mapping over the array, or shows an empty-state message if there are no tasks.
- **TaskItem.jsx** — displays a single task (checkbox, text, delete button) and calls `onToggleTask` / `onDeleteTask` when interacted with.

---

## Tech Stack

- React (functional components + hooks: `useState`)
- Vite (development server and build tool)
- Plain CSS (`App.css`) for styling

---

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── TaskForm.jsx
│   │   ├── TaskItem.jsx
│   │   └── TaskList.jsx
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
├── index.html
├── package.json
└── vite.config.js
```

---

## Run Instructions

1. **Navigate into the frontend folder:**
   ```bash
   cd frontend
   ```

2. **Install dependencies** (only needed once, or after pulling new changes):
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Open the app in your browser:**
   ```
   http://localhost:5173
   ```
   (or whichever port is shown in your terminal — some setups default to `http://localhost:3000`)

5. **Stop the server** when done by pressing `Ctrl + C` in the terminal.

---

## How to Use the App

- Type a task name into the input field and click **Add Task** to add it to the list.
- Click the **checkbox** next to a task to mark it as completed (it will turn green and show "(completed)").
- Click **Delete** to remove a task from the list.
- If all tasks are deleted, an empty-state message ("No tasks yet. Add one above! 🎉") is shown instead of a blank list.

---

## Notes

- Task data is currently stored only in local React state (`useState`) — refreshing the page will reset the list back to the mock/sample tasks.
- No backend calls are made yet — this is intentional per the project requirements for this stage.
- **Planned next step:** connect this frontend to a FastAPI backend by replacing the mock `useState` initial data with a `useEffect` + `fetch` call to load real tasks, and wiring `addTask`, `toggleTask`, and `deleteTask` to call the corresponding API endpoints (POST, PATCH/PUT, DELETE).
=======
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

