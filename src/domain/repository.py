"""
Repository protocol for task persistence.

This module defines the TaskRepository protocol (abstract interface)
that specifies operations for task storage and retrieval.
"""

from typing import Protocol, Optional
from src.domain.task import Task


class TaskRepository(Protocol):
    """
    Abstract interface for task storage operations.

    This protocol defines the contract for task persistence,
    allowing different implementations (in-memory, file, database).
    """

    def add(self, title: str, description: str) -> Task:
        """
        Add a new task with auto-generated ID.

        Args:
            title: Task title (non-empty, max 200 chars)
            description: Task description (max 200 chars, optional)

        Returns:
            Created Task with assigned ID

        Raises:
            InvalidTaskError: If title or description violates constraints
        """
        ...

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: Unique task identifier

        Returns:
            Task if found, None otherwise
        """
        ...

    def get_all(self) -> list[Task]:
        """
        Retrieve all tasks in creation order (by ID).

        Returns:
            List of all tasks (empty list if none exist)
        """
        ...

    def update(
        self,
        task_id: int,
        new_title: Optional[str],
        new_description: Optional[str]
    ) -> Task:
        """
        Update task title and/or description.

        Args:
            task_id: ID of task to update
            new_title: New title (None = keep current)
            new_description: New description (None = keep current)

        Returns:
            Updated Task

        Raises:
            TaskNotFoundError: If task_id does not exist
            InvalidTaskError: If new values violate constraints
        """
        ...

    def delete(self, task_id: int) -> None:
        """
        Delete a task by ID.

        Args:
            task_id: ID of task to delete

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        ...

    def mark_complete(self, task_id: int) -> Task:
        """
        Mark a task as complete.

        Args:
            task_id: ID of task to mark complete

        Returns:
            Updated Task with completed=True

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        ...

    def mark_incomplete(self, task_id: int) -> Task:
        """
        Mark a task as incomplete.

        Args:
            task_id: ID of task to mark incomplete

        Returns:
            Updated Task with completed=False

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        ...
