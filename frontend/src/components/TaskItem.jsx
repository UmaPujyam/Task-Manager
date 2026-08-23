function TaskItem({ task, onToggleTask, onDeleteTask }) {
  return (
    <div className={`task-item ${task.completed ? "completed" : ""}`}>
      <input
        type="checkbox"
        checked={task.completed}
        onChange={() => onToggleTask(task.id)}
      />
      <span>
        {task.text} {task.completed && <em>(completed)</em>}
      </span>
      <button onClick={() => onDeleteTask(task.id)}>Delete</button>
    </div>
  );
}

export default TaskItem;