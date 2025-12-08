# Task Manager - Mid-Project Coursework

A simple command-line task management application built with Python. This project demonstrates object-oriented programming, file I/O, JSON handling, and unit testing.

## Features

- ✅ Add new tasks with titles and descriptions
- ✅ List all tasks or only pending tasks
- ✅ Mark tasks as completed
- ✅ Delete tasks
- ✅ View task statistics
- ✅ Persistent storage using JSON
- ✅ Interactive CLI interface
- ✅ Comprehensive unit tests

## Installation

This project uses only Python standard library, so no additional dependencies are required.

### Requirements
- Python 3.6 or higher

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/nitzannossery/mid-project325694537.git
   cd mid-project325694537
   ```

2. Run the application:
   ```bash
   python task_manager.py
   ```

## Usage

### Running the Task Manager

```bash
python task_manager.py
```

The application will present an interactive menu with the following options:

1. **Add task** - Create a new task with a title and optional description
2. **List tasks** - View all tasks or only pending tasks
3. **Complete task** - Mark a task as completed
4. **Delete task** - Remove a task from the list
5. **View statistics** - See total, completed, and pending task counts
6. **Exit** - Close the application

### Example Session

```
==================================================
Task Manager - Mid-Project Coursework
==================================================

Commands:
  1. Add task
  2. List tasks
  3. Complete task
  4. Delete task
  5. View statistics
  6. Exit

Enter your choice (1-6): 1
Enter task title: Complete homework
Enter task description (optional): Finish math problems 1-10
✓ Task added: [✗] 1. Complete homework
```

## Testing

Run the unit tests to verify the functionality:

```bash
python test_task_manager.py
```

Or with verbose output:

```bash
python test_task_manager.py -v
```

### Test Coverage

The test suite includes:
- Task creation and manipulation
- TaskManager operations (add, get, update, delete, complete)
- List filtering (all tasks vs. pending only)
- Statistics calculation
- Persistent storage (save and load)

## Project Structure

```
mid-project325694537/
│
├── task_manager.py       # Main application with Task and TaskManager classes
├── test_task_manager.py  # Unit tests
├── requirements.txt      # Project dependencies (none required)
├── README.md            # This file
└── tasks.json           # Task storage (created automatically)
```

## Implementation Details

### Task Class
- Represents a single task with ID, title, description, completion status, and creation timestamp
- Methods for converting to/from dictionary for JSON serialization

### TaskManager Class
- Manages a collection of tasks
- Handles persistent storage using JSON files
- Provides CRUD operations (Create, Read, Update, Delete)
- Tracks task IDs automatically

## Features Demonstrated

This project showcases several important programming concepts:

1. **Object-Oriented Programming (OOP)**
   - Classes and objects
   - Encapsulation
   - Type hints

2. **File I/O**
   - Reading and writing JSON files
   - Error handling

3. **Data Structures**
   - Lists and dictionaries
   - Data serialization

4. **Testing**
   - Unit tests with unittest framework
   - Test fixtures and cleanup
   - Test coverage

5. **User Interface**
   - Command-line interface
   - Input validation
   - User-friendly output

## Future Enhancements

Possible improvements for further development:
- Add task priorities
- Set due dates and reminders
- Sort tasks by various criteria
- Export tasks to different formats
- Add categories/tags
- Search functionality
- Task notes and comments

## License

This is a coursework project for educational purposes.

## Author

Created as a mid-project coursework assignment.