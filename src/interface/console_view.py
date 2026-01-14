"""
Console view for displaying output to the user.

This module handles all console output including menus,
task lists, messages, and prompts.
"""

from src.domain.task import Task


class ConsoleView:
    """
    Handles all console output for the Todo application.

    Separates presentation logic from business logic.
    """

    @staticmethod
    def display_menu() -> None:
        """Display the main menu with all available options."""
        print("\n" + "=" * 33)
        print("    TODO APPLICATION")
        print("=" * 33)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print("=" * 33)

    @staticmethod
    def display_task_list(tasks: list[Task]) -> None:
        """
        Display all tasks in formatted list.

        Args:
            tasks: List of tasks to display
        """
        if not tasks:
            print("\nNo tasks found.")
            return

        print()
        for task in tasks:
            status_symbol = "✓" if task.completed else "✗"
            print(f"[{task.id}] {task.title} | {task.description} | {status_symbol}")
            print()

    @staticmethod
    def display_message(message: str) -> None:
        """
        Display a success or informational message.

        Args:
            message: Message to display
        """
        print(f"\n{message}")

    @staticmethod
    def display_error(error_message: str) -> None:
        """
        Display an error message.

        Args:
            error_message: Error message to display (should start with "Error:")
        """
        print(f"\n{error_message}")

    @staticmethod
    def prompt_for_input(prompt: str) -> str:
        """
        Prompt user for input and return the response.

        Args:
            prompt: Prompt message to display

        Returns:
            User input string
        """
        return input(f"\n{prompt}")
