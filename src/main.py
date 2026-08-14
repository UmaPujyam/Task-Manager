from task_manager import TaskManager


def display_menu():
    print("\n===== Task Manager =====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def get_task_id():
    try:
        return int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    task_manager = TaskManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")

            if title.strip():
                task_manager.add_task(title)
            else:
                print("Task title cannot be empty.")

        elif choice == "2":
            task_manager.list_tasks()

        elif choice == "3":
            task_id = get_task_id()

            if task_id is not None:
                task_manager.mark_completed(task_id)

        elif choice == "4":
            task_id = get_task_id()

            if task_id is not None:
                task_manager.delete_task(task_id)

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()