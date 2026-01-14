"""
Update Task use case.

This module implements the business logic for updating task details.
"""

from typing import Optional
from src.domain.task import Task
from src.domain.repository import TaskRepository


class UpdateTaskUseCase:
    """
    Use case for updating an existing task's title and/or description.

    Allows partial updates (only title, only description, or both).
    """

    def __init__(self, repository: TaskRepository) -> None:
        """
        Initialize use case with repository dependency.

        Args:
            repository: Task storage implementation
        """
        self._repository = repository

    def execute(
        self,
        task_id: int,
        new_title: Optional[str],
        new_description: Optional[str]
    ) -> Task:
        """
        Update task with new title and/or description.

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
        return self._repository.update(task_id, new_title, new_description)
