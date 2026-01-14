"""
Delete Task use case.

This module implements the business logic for deleting tasks.
"""

from src.domain.repository import TaskRepository


class DeleteTaskUseCase:
    """
    Use case for deleting a task from the repository.

    Deleted task IDs are never reused.
    """

    def __init__(self, repository: TaskRepository) -> None:
        """
        Initialize use case with repository dependency.

        Args:
            repository: Task storage implementation
        """
        self._repository = repository

    def execute(self, task_id: int) -> None:
        """
        Delete a task by its ID.

        Args:
            task_id: ID of task to delete

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        self._repository.delete(task_id)
