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