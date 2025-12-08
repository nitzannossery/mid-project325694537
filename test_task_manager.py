"""
Unit tests for Task Manager
"""

import unittest
import os
import json
from task_manager import Task, TaskManager


class TestTask(unittest.TestCase):
    """Test cases for Task class"""
    
    def test_task_creation(self):
        """Test creating a task"""
        task = Task(1, "Test Task", "Test Description")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
    
    def test_task_to_dict(self):
        """Test converting task to dictionary"""
        task = Task(1, "Test Task", "Test Description")
        task_dict = task.to_dict()
        self.assertEqual(task_dict['task_id'], 1)
        self.assertEqual(task_dict['title'], "Test Task")
        self.assertEqual(task_dict['description'], "Test Description")
    
    def test_task_from_dict(self):
        """Test creating task from dictionary"""
        data = {
            'task_id': 1,
            'title': "Test Task",
            'description': "Test Description",
            'completed': False,
            'created_at': "2024-01-01T00:00:00"
        }
        task = Task.from_dict(data)
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Test Task")


class TestTaskManager(unittest.TestCase):
    """Test cases for TaskManager class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_file = "test_tasks.json"
        self.manager = TaskManager(self.test_file)
    
    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_task(self):
        """Test adding a task"""
        task = self.manager.add_task("Test Task", "Description")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(len(self.manager.tasks), 1)
    
    def test_get_task(self):
        """Test getting a task by ID"""
        task = self.manager.add_task("Test Task")
        retrieved_task = self.manager.get_task(task.task_id)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.title, "Test Task")
    
    def test_get_nonexistent_task(self):
        """Test getting a non-existent task"""
        task = self.manager.get_task(999)
        self.assertIsNone(task)
    
    def test_complete_task(self):
        """Test completing a task"""
        task = self.manager.add_task("Test Task")
        completed_task = self.manager.complete_task(task.task_id)
        self.assertTrue(completed_task.completed)
    
    def test_delete_task(self):
        """Test deleting a task"""
        task = self.manager.add_task("Test Task")
        result = self.manager.delete_task(task.task_id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 0)
    
    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task"""
        result = self.manager.delete_task(999)
        self.assertFalse(result)
    
    def test_list_tasks(self):
        """Test listing tasks"""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
    
    def test_list_pending_tasks(self):
        """Test listing only pending tasks"""
        task1 = self.manager.add_task("Task 1")
        task2 = self.manager.add_task("Task 2")
        self.manager.complete_task(task1.task_id)
        pending_tasks = self.manager.list_tasks(show_completed=False)
        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(pending_tasks[0].task_id, task2.task_id)
    
    def test_update_task(self):
        """Test updating a task"""
        task = self.manager.add_task("Old Title", "Old Description")
        updated_task = self.manager.update_task(
            task.task_id, 
            title="New Title", 
            description="New Description"
        )
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")
    
    def test_statistics(self):
        """Test getting statistics"""
        task1 = self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.manager.complete_task(task1.task_id)
        
        stats = self.manager.get_statistics()
        self.assertEqual(stats['total'], 2)
        self.assertEqual(stats['completed'], 1)
        self.assertEqual(stats['pending'], 1)
    
    def test_save_and_load(self):
        """Test saving and loading tasks"""
        self.manager.add_task("Task 1", "Description 1")
        self.manager.add_task("Task 2", "Description 2")
        
        # Create new manager instance to test loading
        new_manager = TaskManager(self.test_file)
        self.assertEqual(len(new_manager.tasks), 2)
        self.assertEqual(new_manager.tasks[0].title, "Task 1")


if __name__ == '__main__':
    unittest.main()
