"""
In-memory implementation of TaskRepository.

This module provides an in-memory task storage implementation
using a Python dictionary for fast lookups.
"""

from typing import Optional
from src.domain.task import Task
from src.domain.exceptions import TaskNotFoundError


class InMemoryTaskRepository:
    """
    In-memory task storage with auto-incrementing IDs.

    Tasks are stored in a dictionary keyed by ID. Deleted task IDs
    are never reused (ID counter only increments).
    """

    def __init__(self) -> None:
        """Initialize empty repository with ID counter at 1."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, title: str, description: str) -> Task:
        """Add new task with auto-generated ID."""
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            completed=False
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve task by ID, or None if not found."""
        return self._tasks.get(task_id)

    def get_all(self) -> list[Task]:
        """Return all tasks sorted by ID (creation order)."""
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def update(
        self,
        task_id: int,
        new_title: Optional[str],
        new_description: Optional[str]
    ) -> Task:
        """Update task title and/or description."""
        task = self.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Error: Task #{task_id} not found")

        # Keep current values if new values are None
        updated_title = new_title if new_title is not None else task.title
        updated_desc = new_description if new_description is not None else task.description

        # Create updated task (validates new values)
        updated_task = Task(
            id=task.id,
            title=updated_title,
            description=updated_desc,
            completed=task.completed
        )
        self._tasks[task_id] = updated_task
        return updated_task

    def delete(self, task_id: int) -> None:
        """Delete task by ID."""
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Error: Task #{task_id} not found")
        del self._tasks[task_id]

    def mark_complete(self, task_id: int) -> Task:
        """Mark task as complete."""
        task = self.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Error: Task #{task_id} not found")

        updated_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            completed=True
        )
        self._tasks[task_id] = updated_task
        return updated_task

    def mark_incomplete(self, task_id: int) -> Task:
        """Mark task as incomplete."""
        task = self.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Error: Task #{task_id} not found")

        updated_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            completed=False
        )
        self._tasks[task_id] = updated_task
        return updated_task
