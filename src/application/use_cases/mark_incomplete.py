"""
Mark Task Incomplete use case.

This module implements the business logic for marking tasks as incomplete.
"""

from src.domain.task import Task
from src.domain.repository import TaskRepository


class MarkIncompleteUseCase:
    """
    Use case for marking a task as incomplete.

    Sets the task's completed status to False.
    """

    def __init__(self, repository: TaskRepository) -> None:
        """
        Initialize use case with repository dependency.

        Args:
            repository: Task storage implementation
        """
        self._repository = repository

    def execute(self, task_id: int) -> Task:
        """
        Mark a task as incomplete.

        Args:
            task_id: ID of task to mark incomplete

        Returns:
            Updated Task with completed=False

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        return self._repository.mark_incomplete(task_id)
