"""
Task entity for the Todo application.

This module defines the Task dataclass representing a todo item with
validation logic for title and description constraints.
"""

from dataclasses import dataclass
from src.domain.exceptions import InvalidTaskError


MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 200


@dataclass
class Task:
    """
    Represents a todo task with title, description, and completion status.

    Attributes:
        id: Unique task identifier (auto-assigned by repository)
        title: Task name (1-200 characters)
        description: Task details (0-200 characters, optional)
        completed: Completion status (False by default)
    """
    id: int
    title: str
    description: str
    completed: bool = False

    def __post_init__(self) -> None:
        """Validate task data after initialization."""
        self._validate_title()
        self._validate_description()

    def _validate_title(self) -> None:
        """
        Validate task title is non-empty and within length limit.

        Raises:
            InvalidTaskError: If title is empty or exceeds 200 characters
        """
        if not self.title or self.title.strip() == "":
            raise InvalidTaskError("Error: Task title cannot be empty")
        if len(self.title) > MAX_TITLE_LENGTH:
            raise InvalidTaskError(
                f"Error: Task title cannot exceed {MAX_TITLE_LENGTH} characters"
            )

    def _validate_description(self) -> None:
        """
        Validate task description is within length limit.

        Raises:
            InvalidTaskError: If description exceeds 200 characters
        """
        if len(self.description) > MAX_DESCRIPTION_LENGTH:
            raise InvalidTaskError(
                f"Error: Task description cannot exceed {MAX_DESCRIPTION_LENGTH} characters"
            )
