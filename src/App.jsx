import { useState } from "react";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Learn React", completed: false },
    { id: 2, text: "Build Task Manager", completed: true },
    { id: 3, text: "Connect to FastAPI", completed: false },
  ]);

  // Add a new task
  const addTask = (text) => {
    const newTask = {
      id: Date.now(), // simple unique id for mock data
      text,
      completed: false,
    };
    setTasks([...tasks, newTask]);
  };

  // Toggle a task's completed status
  const toggleTask = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  // Delete a task
  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  return (
    <div className="app">
      <h1>Task Manager</h1>
      <TaskForm onAddTask={addTask} />
      <TaskList tasks={tasks} onToggleTask={toggleTask} onDeleteTask={deleteTask} />
    </div>
  );
}

export default App;