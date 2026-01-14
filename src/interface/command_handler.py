"""
Command handler for coordinating CLI operations.

This module orchestrates user interactions by coordinating
input validation, use case execution, and output display.
"""

from typing import Optional
from src.application.use_cases import (
    AddTaskUseCase,
    ViewTasksUseCase,
    UpdateTaskUseCase,
    DeleteTaskUseCase,
    MarkCompleteUseCase,
    MarkIncompleteUseCase
)
from src.interface.console_view import ConsoleView
from src.interface.input_validator import InputValidator
from src.domain.exceptions import TodoAppError


class CommandHandler:
    """
    Handles user commands and coordinates application flow.

    Separates CLI logic from business logic by delegating
    to use cases and managing user interaction flow.
    """

    def __init__(
        self,
        add_task_uc: AddTaskUseCase,
        view_tasks_uc: ViewTasksUseCase,
        update_task_uc: UpdateTaskUseCase,
        delete_task_uc: DeleteTaskUseCase,
        mark_complete_uc: MarkCompleteUseCase,
        mark_incomplete_uc: MarkIncompleteUseCase,
        view: ConsoleView,
        validator: InputValidator
    ) -> None:
        """Initialize handler with use cases and view dependencies."""
        self._add_task = add_task_uc
        self._view_tasks = view_tasks_uc
        self._update_task = update_task_uc
        self._delete_task = delete_task_uc
        self._mark_complete = mark_complete_uc
        self._mark_incomplete = mark_incomplete_uc
        self._view = view
        self._validator = validator

    def handle_add_task(self) -> None:
        """Handle the Add Task command."""
        try:
            title = self._view.prompt_for_input("Enter task title: ")
            description = self._view.prompt_for_input("Enter task description: ")
            task = self._add_task.execute(title, description)
            self._view.display_message(f"Task #{task.id} added successfully")
        except TodoAppError as e:
            self._view.display_error(str(e))

    def handle_view_tasks(self) -> None:
        """Handle the View Tasks command."""
        tasks = self._view_tasks.execute()
        self._view.display_task_list(tasks)

    def handle_update_task(self) -> None:
        """Handle the Update Task command."""
        try:
            id_str = self._view.prompt_for_input("Enter task ID to update: ")
            task_id = self._validator.validate_task_id(id_str)

            title_input = self._view.prompt_for_input(
                "Enter new title (or press Enter to keep current): "
            )
            new_title: Optional[str] = title_input if title_input.strip() else None

            desc_input = self._view.prompt_for_input(
                "Enter new description (or press Enter to keep current): "
            )
            new_desc: Optional[str] = desc_input if desc_input.strip() else None

            self._update_task.execute(task_id, new_title, new_desc)
            self._view.display_message(f"Task #{task_id} updated successfully")
        except TodoAppError as e:
            self._view.display_error(str(e))

    def handle_delete_task(self) -> None:
        """Handle the Delete Task command."""
        try:
            id_str = self._view.prompt_for_input("Enter task ID to delete: ")
            task_id = self._validator.validate_task_id(id_str)
            self._delete_task.execute(task_id)
            self._view.display_message(f"Task #{task_id} deleted successfully")
        except TodoAppError as e:
            self._view.display_error(str(e))

    def handle_mark_complete(self) -> None:
        """Handle the Mark Task Complete command."""
        try:
            id_str = self._view.prompt_for_input("Enter task ID: ")
            task_id = self._validator.validate_task_id(id_str)
            self._mark_complete.execute(task_id)
            self._view.display_message(f"Task #{task_id} marked as complete")
        except TodoAppError as e:
            self._view.display_error(str(e))

    def handle_mark_incomplete(self) -> None:
        """Handle the Mark Task Incomplete command."""
        try:
            id_str = self._view.prompt_for_input("Enter task ID: ")
            task_id = self._validator.validate_task_id(id_str)
            self._mark_incomplete.execute(task_id)
            self._view.display_message(f"Task #{task_id} marked as incomplete")
        except TodoAppError as e:
            self._view.display_error(str(e))

    def handle_exit(self) -> bool:
        """
        Handle the Exit command.

        Returns:
            True to indicate application should exit
        """
        self._view.display_message("Goodbye!")
        return True
