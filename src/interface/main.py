"""
Main application entry point.

This module sets up dependencies and runs the main CLI loop.
"""

from src.application.repository import InMemoryTaskRepository
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
from src.interface.command_handler import CommandHandler
from src.domain.exceptions import InvalidCommandError


def main() -> None:
    """
    Main application loop.

    Initializes dependencies, displays menu, and dispatches commands
    until user selects Exit.
    """
    # Initialize repository
    repository = InMemoryTaskRepository()

    # Initialize use cases
    add_task_uc = AddTaskUseCase(repository)
    view_tasks_uc = ViewTasksUseCase(repository)
    update_task_uc = UpdateTaskUseCase(repository)
    delete_task_uc = DeleteTaskUseCase(repository)
    mark_complete_uc = MarkCompleteUseCase(repository)
    mark_incomplete_uc = MarkIncompleteUseCase(repository)

    # Initialize view and validator
    view = ConsoleView()
    validator = InputValidator()

    # Initialize command handler
    handler = CommandHandler(
        add_task_uc,
        view_tasks_uc,
        update_task_uc,
        delete_task_uc,
        mark_complete_uc,
        mark_incomplete_uc,
        view,
        validator
    )

    # Main loop
    while True:
        view.display_menu()
        choice_str = view.prompt_for_input("Enter your choice (1-7): ")

        try:
            choice = validator.validate_menu_choice(choice_str)

            if choice == 1:
                handler.handle_add_task()
            elif choice == 2:
                handler.handle_view_tasks()
            elif choice == 3:
                handler.handle_update_task()
            elif choice == 4:
                handler.handle_delete_task()
            elif choice == 5:
                handler.handle_mark_complete()
            elif choice == 6:
                handler.handle_mark_incomplete()
            elif choice == 7:
                should_exit = handler.handle_exit()
                if should_exit:
                    break

        except InvalidCommandError as e:
            view.display_error(str(e))


if __name__ == "__main__":
    main()
