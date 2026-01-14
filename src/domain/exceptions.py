"""
Domain exceptions for the Todo application.

This module defines custom exceptions used throughout the domain layer,
providing clear error semantics for task-related operations.
"""


class TodoAppError(Exception):
    """Base exception for all todo application errors."""
    pass


class InvalidTaskError(TodoAppError):
    """Raised when task data is invalid (empty title, exceeds length limits)."""
    pass


class TaskNotFoundError(TodoAppError):
    """Raised when a task with the specified ID does not exist."""
    pass


class InvalidCommandError(TodoAppError):
    """Raised when user provides an invalid command or menu choice."""
    pass
