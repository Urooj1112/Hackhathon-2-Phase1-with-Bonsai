"""
Add Task use case.

This module implements the business logic for adding a new task.
"""

from src.domain.task import Task
from src.domain.repository import TaskRepository


class AddTaskUseCase:
    """
    Use case for adding a new task to the repository.

    Coordinates validation and persistence of new tasks.
    """

    def __init__(self, repository: TaskRepository) -> None:
        """
        Initialize use case with repository dependency.

        Args:
            repository: Task storage implementation
        """
        self._repository = repository

    def execute(self, title: str, description: str) -> Task:
        """
        Add a new task with the given title and description.

        Args:
            title: Task title (validated by Task entity)
            description: Task description (validated by Task entity)

        Returns:
            Created Task with assigned ID

        Raises:
            InvalidTaskError: If title or description violates constraints
        """
        return self._repository.add(title, description)
