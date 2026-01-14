"""
Mark Task Complete use case.

This module implements the business logic for marking tasks as complete.
"""

from src.domain.task import Task
from src.domain.repository import TaskRepository


class MarkCompleteUseCase:
    """
    Use case for marking a task as complete.

    Sets the task's completed status to True.
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
        Mark a task as complete.

        Args:
            task_id: ID of task to mark complete

        Returns:
            Updated Task with completed=True

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        return self._repository.mark_complete(task_id)
