# Task Manager - Mid-Project Coursework

A simple command-line task management application built with Python. This project demonstrates object-oriented programming, file I/O, JSON handling, and unit testing.

## Components

### 1. Task Manager Application
A complete task management CLI application with persistent storage.

### 2. Yahoo Finance Integration
A script to fetch stock market data using the yfinance library.

## Features

### Task Manager Features
- ✅ Add new tasks with titles and descriptions
- ✅ List all tasks or only pending tasks
- ✅ Mark tasks as completed
- ✅ Delete tasks
- ✅ View task statistics
- ✅ Persistent storage using JSON
- ✅ Interactive CLI interface
- ✅ Comprehensive unit tests

### Yahoo Finance Features
- ✅ Fetch current stock prices
- ✅ Get market capitalization
- ✅ Download historical data
- ✅ Support for multiple stock tickers

## Installation

### Requirements
- Python 3.6 or higher
- pip (Python package installer)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/nitzannossery/mid-project325694537.git
   cd mid-project325694537
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Task Manager

Run the application:
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

### Yahoo Finance

Run the Yahoo Finance script:

```bash
python yahoo_finance.py
```

The script will:
- Fetch Apple (AAPL) stock information including current price and market cap
- Display historical price data for the last month
- Download and display closing prices for Apple, Microsoft, and Google for the past year

Example output:
```
150.25
2450000000000
                Open      High       Low     Close    Volume
Date                                                         
2024-12-20   148.50   151.20   147.80   150.25  50000000
...
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
├── task_manager.py       # Main task management application
├── test_task_manager.py  # Unit tests for task manager
├── yahoo_finance.py      # Yahoo Finance stock data fetcher
├── requirements.txt      # Project dependencies
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

1. **Object-Oriented Programming (OOP)** - Task Manager
   - Classes and objects
   - Encapsulation
   - Type hints

2. **File I/O** - Task Manager
   - Reading and writing JSON files
   - Error handling

3. **Data Structures** - Task Manager
   - Lists and dictionaries
   - Data serialization

4. **Testing** - Task Manager
   - Unit tests with unittest framework
   - Test fixtures and cleanup
   - Test coverage

5. **User Interface** - Task Manager
   - Command-line interface
   - Input validation
   - User-friendly output

6. **External APIs** - Yahoo Finance
   - Working with third-party libraries (yfinance)
   - Fetching real-time financial data
   - Data visualization with pandas

## Future Enhancements

### Task Manager
- Add task priorities
- Set due dates and reminders
- Sort tasks by various criteria
- Export tasks to different formats
- Add categories/tags
- Search functionality
- Task notes and comments

### Yahoo Finance
- Add more stock tickers
- Create visualizations and charts
- Calculate technical indicators
- Set up price alerts
- Portfolio tracking

## License

This is a coursework project for educational purposes.

## Author

Created as a mid-project coursework assignment.