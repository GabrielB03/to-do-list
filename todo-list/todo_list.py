import json
from typing import List, Dict

# Type alias for a task
Task = Dict[str, bool]

def load_tasks(filename: str = 'tasks.json') -> List[Task]:
    """Load tasks from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks: List[Task], filename: str = 'tasks.json') -> None:
    """Save tasks to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
        
def display_tasks(tasks: List[Task]) -> None:
    """Display tasks with their completion status."""
    for idx, task in enumerate(tasks):
        status = 'Completed' if task['completed'] else 'Pending'
        print(f"´{idx + 1}. {task['title']} - {status}")
        
def add_task(tasks: List[Task], title: str) -> None:
    """Add a new task."""
    tasks.append({'title': title, 'completed': False}) # type: ignore
    
def complete_task(tasks: List[Task], index: int) -> None:
    """Mark a task as completed."""
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
    else:
        raise IndexError("Task index out of range.")
    
def main() -> None:
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. View Tasks\n4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            title = input("Enter task title: ").strip()
            add_task(tasks, title)
        elif choice == '2':
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to complete: ")) - 1
                complete_task(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            except IndexError as e:
                print(e)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()