"""
Input validation utilities for the CLI.

This module provides validation functions for user inputs
including task IDs, titles, and descriptions.
"""

from src.domain.exceptions import InvalidTaskError


class InputValidator:
    """
    Validates user input for CLI commands.

    Ensures inputs meet domain constraints before processing.
    """

    @staticmethod
    def validate_task_id(id_str: str) -> int:
        """
        Validate and convert task ID string to positive integer.

        Args:
            id_str: User input string for task ID

        Returns:
            Validated task ID as integer

        Raises:
            InvalidTaskError: If ID is not a positive integer
        """
        try:
            task_id = int(id_str)
            if task_id <= 0:
                raise ValueError
            return task_id
        except ValueError:
            raise InvalidTaskError("Error: Task ID must be a positive integer")

    @staticmethod
    def validate_menu_choice(choice_str: str) -> int:
        """
        Validate menu choice is an integer between 1 and 7.

        Args:
            choice_str: User input string for menu choice

        Returns:
            Validated menu choice as integer

        Raises:
            InvalidTaskError: If choice is not 1-7
        """
        try:
            choice = int(choice_str)
            if choice < 1 or choice > 7:
                raise ValueError
            return choice
        except ValueError:
            raise InvalidTaskError("Error: Invalid choice. Please enter 1-7")
