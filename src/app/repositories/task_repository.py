from app.database import get_connection
from app.models.task import Task

class TaskRepository:
    def get_all(self) -> list[Task]:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, title, completed FROM tasks ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [Task(id=r[0], title=r[1], completed=r[2]) for r in rows]

    def get_by_id(self, task_id: int) -> Task | None:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, title, completed FROM tasks WHERE id = %s",
            (task_id,)
        )
        row = cur.fetchone()
        cur.close()
        conn.close()
        return Task(id=row[0], title=row[1], completed=row[2]) if row else None

    def create(self, title: str) -> Task:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title, completed",
            (title,)
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return Task(id=row[0], title=row[1], completed=row[2])

    def update(self, task_id: int, title: str, completed: bool) -> Task | None:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE tasks SET title = %s, completed = %s
            WHERE id = %s
            RETURNING id, title, completed
            """,
            (title, completed, task_id)
        )
        row = cur.fetchone()
        if row is None:
            cur.close()
            conn.close()
            return None
        conn.commit()
        cur.close()
        conn.close()
        return Task(id=row[0], title=row[1], completed=row[2])

    def delete(self, task_id: int) -> bool:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s RETURNING id", (task_id,))
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return row is not None