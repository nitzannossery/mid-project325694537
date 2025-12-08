"""
Task Manager - A simple command-line task management application
This is a mid-project coursework implementation
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class Task:
    """Represents a single task"""
    
    def __init__(self, task_id: int, title: str, description: str = "", 
                 completed: bool = False, created_at: str = None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary"""
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary"""
        return cls(**data)
    
    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.task_id}. {self.title}"


class TaskManager:
    """Manages a collection of tasks"""
    
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def load_tasks(self) -> None:
        """Load tasks from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
                    if self.tasks:
                        self.next_id = max(task.task_id for task in self.tasks) + 1
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
    
    def save_tasks(self) -> None:
        """Save tasks to file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task"""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        task = Task(self.next_id, title.strip(), description.strip())
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: str = None, 
                    description: str = None) -> Optional[Task]:
        """Update a task"""
        task = self.get_task(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            self.save_tasks()
        return task
    
    def complete_task(self, task_id: int) -> Optional[Task]:
        """Mark a task as completed"""
        task = self.get_task(task_id)
        if task:
            task.completed = True
            self.save_tasks()
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False
    
    def list_tasks(self, show_completed: bool = True) -> List[Task]:
        """List all tasks"""
        if show_completed:
            return self.tasks
        return [task for task in self.tasks if not task.completed]
    
    def get_statistics(self) -> Dict:
        """Get task statistics"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        pending = total - completed
        return {
            'total': total,
            'completed': completed,
            'pending': pending
        }


def main():
    """Main CLI interface"""
    manager = TaskManager()
    
    print("=" * 50)
    print("Task Manager - Mid-Project Coursework")
    print("=" * 50)
    
    while True:
        print("\nCommands:")
        print("  1. Add task")
        print("  2. List tasks")
        print("  3. Complete task")
        print("  4. Delete task")
        print("  5. View statistics")
        print("  6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                continue
            description = input("Enter task description (optional): ").strip()
            try:
                task = manager.add_task(title, description)
                print(f"✓ Task added: {task}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            show_all = input("Show completed tasks? (y/n): ").strip().lower() == 'y'
            tasks = manager.list_tasks(show_completed=show_all)
            if tasks:
                print("\nTasks:")
                for task in tasks:
                    print(f"  {task}")
                    if task.description:
                        print(f"    Description: {task.description}")
            else:
                print("No tasks found.")
        
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: ").strip())
                task = manager.complete_task(task_id)
                if task:
                    print(f"✓ Task completed: {task}")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid task ID.")
        
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                if manager.delete_task(task_id):
                    print("✓ Task deleted.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid task ID.")
        
        elif choice == "5":
            stats = manager.get_statistics()
            print("\nStatistics:")
            print(f"  Total tasks: {stats['total']}")
            print(f"  Completed: {stats['completed']}")
            print(f"  Pending: {stats['pending']}")
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
