"""
View Tasks use case.

This module implements the business logic for retrieving all tasks.
"""

from src.domain.task import Task
from src.domain.repository import TaskRepository


class ViewTasksUseCase:
    """
    Use case for retrieving all tasks from the repository.

    Returns tasks in creation order (sorted by ID).
    """

    def __init__(self, repository: TaskRepository) -> None:
        """
        Initialize use case with repository dependency.

        Args:
            repository: Task storage implementation
        """
        self._repository = repository

    def execute(self) -> list[Task]:
        """
        Retrieve all tasks.

        Returns:
            List of all tasks in ID order (empty if none exist)
        """
        return self._repository.get_all()
