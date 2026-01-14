# Feature Specification: Core Todo Operations

**Feature Branch**: `001-core-todo-operations`
**Created**: 2026-01-08
**Status**: Draft
**Input**: User description: "Phase-I Todo Console App with Add, View, Update, Delete, and Mark Complete/Incomplete features"

## Overview

This specification defines a console-based Python todo application that stores tasks in memory. The application provides a menu-driven CLI interface for managing todo tasks with five core operations: add, view, update, delete, and toggle completion status. The system maintains tasks until program termination (no persistence in Phase I).

**Constitutional Alignment**:
- **Principle I (Spec-Driven Development)**: This spec defines all functionality before code generation
- **Principle II (Clean Architecture)**: Separates domain (Task), application (use cases), and interface (CLI) concerns
- **Principle V (Deterministic Behavior)**: Task IDs auto-increment predictably from 1
- **Principle VI (Defensive Input Handling)**: All inputs validated with explicit error messages

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create and View First Task (Priority: P1)

A user launches the application and wants to add their first todo item and see it displayed.

**Why this priority**: Foundation for all other operations. Without the ability to add and view tasks, the application has no value.

**Independent Test**: Can be fully tested by launching app, adding one task, viewing the list, and confirming the task appears with correct ID, title, description, and incomplete status.

**Acceptance Scenarios**:

1. **Given** the application is running with no tasks, **When** user selects "Add Task" and enters title "Buy groceries" and description "Milk, eggs, bread", **Then** system displays "Task #1 added successfully" and returns to main menu
2. **Given** one task exists (ID=1, title="Buy groceries"), **When** user selects "View Tasks", **Then** system displays task with ID=1, title="Buy groceries", description="Milk, eggs, bread", and status="✗" (incomplete)
3. **Given** the application is running with no tasks, **When** user selects "View Tasks", **Then** system displays "No tasks found." and returns to main menu

---

### User Story 2 - Toggle Task Completion (Priority: P2)

A user has added tasks and wants to mark one as complete when finished, then later mark it incomplete if they need to redo it.

**Why this priority**: Core workflow—users need to track progress. Marking tasks complete is the primary value proposition of a todo app.

**Independent Test**: Can be fully tested by adding one task, marking it complete, verifying status changes to "✓", marking it incomplete, and verifying status reverts to "✗".

**Acceptance Scenarios**:

1. **Given** task #1 exists with status incomplete (✗), **When** user selects "Mark Complete" and enters ID=1, **Then** system displays "Task #1 marked as complete" and status changes to ✓
2. **Given** task #1 exists with status complete (✓), **When** user selects "Mark Incomplete" and enters ID=1, **Then** system displays "Task #1 marked as incomplete" and status changes to ✗
3. **Given** no tasks exist, **When** user selects "Mark Complete" and enters ID=1, **Then** system displays "Error: Task #1 not found" and returns to main menu
4. **Given** tasks #1 and #2 exist, **When** user selects "Mark Complete" and enters ID=99, **Then** system displays "Error: Task #99 not found"

---

### User Story 3 - Update Task Details (Priority: P3)

A user has added a task with incorrect or incomplete information and wants to fix the title or description without deleting and recreating the task.

**Why this priority**: Improves usability and reduces friction. Users often need to clarify or correct task details as they refine their workflow.

**Independent Test**: Can be fully tested by adding one task, updating its title only, verifying the change, then updating its description, and confirming both fields are correct.

**Acceptance Scenarios**:

1. **Given** task #1 exists with title="Buy groceries" and description="Milk, eggs", **When** user selects "Update Task", enters ID=1, new title="Buy groceries today", and keeps description unchanged, **Then** system displays "Task #1 updated successfully" and task now has title="Buy groceries today" with original description preserved
2. **Given** task #1 exists, **When** user selects "Update Task", enters ID=1, keeps title unchanged, and enters new description="Milk, eggs, bread, butter", **Then** system displays "Task #1 updated successfully" and task has original title with new description
3. **Given** task #1 exists, **When** user selects "Update Task", enters ID=1, new title="Go shopping", and new description="Updated list", **Then** both fields are updated simultaneously
4. **Given** no tasks exist, **When** user selects "Update Task" and enters ID=1, **Then** system displays "Error: Task #1 not found"
5. **Given** tasks exist, **When** user selects "Update Task", enters ID=5 (invalid), **Then** system displays "Error: Task #5 not found"

---

### User Story 4 - Delete Completed Tasks (Priority: P3)

A user has completed tasks and wants to remove them to keep the task list focused on active items.

**Why this priority**: Cleanup operation for maintaining a manageable task list. Less critical than creation and completion workflows.

**Independent Test**: Can be fully tested by adding two tasks, deleting one by ID, verifying it no longer appears in the list, and confirming the other task remains.

**Acceptance Scenarios**:

1. **Given** task #1 exists with title="Buy groceries", **When** user selects "Delete Task" and enters ID=1, **Then** system displays "Task #1 deleted successfully" and task no longer appears in view list
2. **Given** tasks #1, #2, #3 exist, **When** user deletes task #2, **Then** tasks #1 and #3 remain visible with their original IDs (IDs are not reassigned)
3. **Given** no tasks exist, **When** user selects "Delete Task" and enters ID=1, **Then** system displays "Error: Task #1 not found"
4. **Given** tasks #1 and #2 exist, **When** user selects "Delete Task" and enters ID=99, **Then** system displays "Error: Task #99 not found" and no tasks are deleted

---

### User Story 5 - Exit Application Gracefully (Priority: P1)

A user finishes managing tasks and wants to cleanly exit the application.

**Why this priority**: Essential for user control and clean program termination. Without explicit exit, users cannot control the application lifecycle.

**Independent Test**: Can be fully tested by launching app, performing any operations, selecting "Exit", and confirming program terminates without errors or prompts.

**Acceptance Scenarios**:

1. **Given** the application is running (with or without tasks), **When** user selects "Exit" from main menu, **Then** system displays "Goodbye!" and program terminates cleanly
2. **Given** user is in the middle of adding a task, **When** user navigates back to main menu and selects "Exit", **Then** program terminates without saving incomplete task entry

---

### Edge Cases

- **Empty title input**: What happens when user enters blank/whitespace-only title during Add or Update?
- **Empty description input**: What happens when user enters blank description during Add or Update?
- **Title/description length limits**: How does system handle titles or descriptions exceeding 200 characters?
- **Non-integer task ID input**: What happens when user enters "abc" or "1.5" for task ID in Update/Delete/Mark Complete?
- **Negative task ID input**: What happens when user enters -1 for task ID?
- **Zero task ID input**: What happens when user enters 0 for task ID?
- **Invalid menu selection**: What happens when user enters invalid menu option (e.g., "99" or "xyz")?
- **Maximum tasks**: What happens when 1000+ tasks exist? (Performance boundary, not enforced limit)
- **Rapid sequential operations**: Can user add 10 tasks, delete 5, update 3, and mark 2 complete without errors?
- **ID reuse after deletion**: If task #5 is deleted, is ID 5 reused for the next added task, or does ID continue incrementing?

## Requirements *(mandatory)*

### Functional Requirements

#### Core Operations

- **FR-001**: System MUST allow users to add a new task by providing a title and description
- **FR-002**: System MUST display a list of all tasks showing ID, title, description, and completion status
- **FR-003**: System MUST allow users to update the title and/or description of an existing task by task ID
- **FR-004**: System MUST allow users to delete a task by task ID
- **FR-005**: System MUST allow users to mark a task as complete by task ID
- **FR-006**: System MUST allow users to mark a task as incomplete by task ID
- **FR-007**: System MUST provide a menu-driven interface with options for all operations plus Exit

#### Task Management

- **FR-008**: System MUST assign unique, auto-incrementing integer IDs to tasks starting from 1
- **FR-009**: System MUST store all tasks in memory (no file or database persistence)
- **FR-010**: System MUST maintain task IDs permanently (deleted task IDs are not reused)
- **FR-011**: System MUST initialize each new task with completion status = incomplete (✗)
- **FR-012**: System MUST preserve task order by creation time (tasks displayed in ID order)

#### Input Validation

- **FR-013**: System MUST reject empty or whitespace-only task titles with error message: "Error: Task title cannot be empty"
- **FR-014**: System MUST accept empty descriptions (descriptions are optional)
- **FR-015**: System MUST reject task titles exceeding 200 characters with error message: "Error: Task title cannot exceed 200 characters"
- **FR-016**: System MUST reject task descriptions exceeding 200 characters with error message: "Error: Task description cannot exceed 200 characters"
- **FR-017**: System MUST validate task IDs are positive integers, rejecting non-integer, zero, or negative values with error message: "Error: Task ID must be a positive integer"
- **FR-018**: System MUST validate task IDs exist before performing operations, displaying "Error: Task #[ID] not found" if invalid

#### User Interaction

- **FR-019**: System MUST display the main menu after every completed operation
- **FR-020**: System MUST display clear prompts for all user inputs (e.g., "Enter task title: ")
- **FR-021**: System MUST display confirmation messages after successful operations (e.g., "Task #5 added successfully")
- **FR-022**: System MUST display error messages without exposing stack traces or internal details
- **FR-023**: System MUST run continuously until user selects "Exit" option
- **FR-024**: System MUST display "Goodbye!" message before terminating

#### Data Display Format

- **FR-025**: System MUST display tasks in the format: `[ID] Title | Description | Status`
- **FR-026**: System MUST use "✓" symbol for completed tasks and "✗" symbol for incomplete tasks
- **FR-027**: System MUST display "No tasks found." when task list is empty
- **FR-028**: System MUST separate multiple tasks with blank lines for readability

### Key Entities *(include if feature involves data)*

- **Task**: Represents a todo item with the following attributes:
  - **id** (integer): Unique, auto-incrementing identifier starting from 1; never reused after deletion
  - **title** (string): Non-empty task name, max 200 characters; describes what needs to be done
  - **description** (string): Optional task details, max 200 characters; provides additional context
  - **completed** (boolean): Completion status; False (✗) by default, toggles to True (✓) when marked complete

- **TaskRepository**: Abstract storage interface for task persistence
  - Phase I implementation: `InMemoryTaskRepository` using Python list
  - Responsibilities: add, retrieve, update, delete tasks; generate unique IDs
  - Guarantees: ID uniqueness, ID immutability after assignment

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: User can add a task, view it in the list, mark it complete, and delete it without encountering errors (happy path completion in under 30 seconds)
- **SC-002**: System rejects 100% of invalid inputs (empty titles, non-integer IDs, IDs exceeding valid range) with actionable error messages
- **SC-003**: System handles 100 tasks without performance degradation (operations complete in <1 second)
- **SC-004**: Application runs continuously for 50+ operations without crashes or memory leaks
- **SC-005**: All error messages are user-friendly (no stack traces, technical jargon, or "Unknown error" messages)
- **SC-006**: Task IDs remain stable—deleting task #5 does not change IDs of tasks #1-4 or #6+

### Quality Gates

- **QG-001**: 100% test coverage for domain layer (Task entity, validation logic)
- **QG-002**: 100% test coverage for application layer (all use cases: add, view, update, delete, mark complete/incomplete)
- **QG-003**: >80% test coverage for interface layer (CLI menu, input parsing, output formatting)
- **QG-004**: All tests pass before code review
- **QG-005**: No `# type: ignore` comments or type hint bypasses
- **QG-006**: Maximum function length: 25 lines (excluding docstrings)
- **QG-007**: Maximum class methods: 7 (excluding `__init__`, `__repr__`)

## User Interaction Flow

### Main Menu Structure

```
=================================
    TODO APPLICATION
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=================================
Enter your choice (1-7): _
```

### Flow Diagrams (Conceptual)

#### Add Task Flow
1. User selects "1. Add Task" from main menu
2. System prompts: "Enter task title: "
3. User enters title
4. System validates title (non-empty, ≤200 chars)
5. System prompts: "Enter task description: "
6. User enters description
7. System validates description (≤200 chars)
8. System creates task with auto-incremented ID
9. System displays: "Task #[ID] added successfully"
10. System returns to main menu

#### View Tasks Flow
1. User selects "2. View Tasks" from main menu
2. System retrieves all tasks from repository
3. If no tasks exist: display "No tasks found."
4. If tasks exist: display each task in format `[ID] Title | Description | Status`
5. System returns to main menu

#### Update Task Flow
1. User selects "3. Update Task" from main menu
2. System prompts: "Enter task ID to update: "
3. User enters task ID
4. System validates ID (positive integer, task exists)
5. System prompts: "Enter new title (or press Enter to keep current): "
6. User enters new title or presses Enter
7. System prompts: "Enter new description (or press Enter to keep current): "
8. User enters new description or presses Enter
9. System validates inputs and updates task
10. System displays: "Task #[ID] updated successfully"
11. System returns to main menu

#### Delete Task Flow
1. User selects "4. Delete Task" from main menu
2. System prompts: "Enter task ID to delete: "
3. User enters task ID
4. System validates ID (positive integer, task exists)
5. System removes task from repository
6. System displays: "Task #[ID] deleted successfully"
7. System returns to main menu

#### Mark Complete/Incomplete Flow
1. User selects "5. Mark Task Complete" or "6. Mark Task Incomplete"
2. System prompts: "Enter task ID: "
3. User enters task ID
4. System validates ID (positive integer, task exists)
5. System toggles task completion status
6. System displays: "Task #[ID] marked as complete" (or "incomplete")
7. System returns to main menu

#### Exit Flow
1. User selects "7. Exit" from main menu
2. System displays: "Goodbye!"
3. Program terminates

## Error Handling Rules

### Input Validation Errors

| Error Condition | Error Message | Recovery Action |
|----------------|---------------|-----------------|
| Empty task title | `Error: Task title cannot be empty` | Re-prompt for title |
| Title exceeds 200 chars | `Error: Task title cannot exceed 200 characters` | Re-prompt for title |
| Description exceeds 200 chars | `Error: Task description cannot exceed 200 characters` | Re-prompt for description |
| Non-integer task ID | `Error: Task ID must be a positive integer` | Re-prompt for ID |
| Zero or negative task ID | `Error: Task ID must be a positive integer` | Re-prompt for ID |
| Task ID not found | `Error: Task #[ID] not found` | Return to main menu |
| Invalid menu choice | `Error: Invalid choice. Please enter 1-7` | Re-prompt for menu selection |

### Error Handling Principles

1. **No Stack Traces**: User-facing errors MUST NOT display Python tracebacks
2. **Actionable Messages**: Errors MUST explain what went wrong and how to fix it
3. **Graceful Degradation**: Invalid operations MUST NOT crash the program
4. **Consistent Format**: All error messages MUST start with "Error: "
5. **Recovery Path**: After error display, system MUST return to a stable state (main menu or re-prompt)

## Acceptance Criteria (Given/When/Then)

### Add Task

**AC-001**: Adding valid task
- **Given** the application is running
- **When** user selects "Add Task", enters title="Write report" and description="Q4 summary"
- **Then** system assigns ID=1 (if first task), displays "Task #1 added successfully", and task appears in View Tasks with status ✗

**AC-002**: Adding task with empty title
- **Given** the application is running
- **When** user selects "Add Task" and enters empty string for title
- **Then** system displays "Error: Task title cannot be empty" and re-prompts for title

**AC-003**: Adding task with title exceeding limit
- **Given** the application is running
- **When** user enters title with 201 characters
- **Then** system displays "Error: Task title cannot exceed 200 characters" and re-prompts

**AC-004**: Adding task with empty description
- **Given** the application is running
- **When** user enters valid title and empty description
- **Then** system accepts empty description and creates task successfully

### View Tasks

**AC-005**: Viewing empty task list
- **Given** no tasks have been added
- **When** user selects "View Tasks"
- **Then** system displays "No tasks found." and returns to main menu

**AC-006**: Viewing multiple tasks
- **Given** three tasks exist (ID=1, 2, 3)
- **When** user selects "View Tasks"
- **Then** system displays all three tasks in ID order with correct titles, descriptions, and status symbols

**AC-007**: Viewing tasks with mixed completion status
- **Given** task #1 is incomplete (✗) and task #2 is complete (✓)
- **When** user selects "View Tasks"
- **Then** system displays both tasks with correct status symbols

### Update Task

**AC-008**: Updating task title only
- **Given** task #1 exists with title="Old Title" and description="Old Desc"
- **When** user updates task #1 with new title="New Title" and presses Enter for description
- **Then** task #1 has title="New Title" and description="Old Desc" (unchanged)

**AC-009**: Updating task description only
- **Given** task #1 exists
- **When** user presses Enter for title and enters new description
- **Then** task #1 keeps original title and has new description

**AC-010**: Updating non-existent task
- **Given** only task #1 exists
- **When** user attempts to update task #5
- **Then** system displays "Error: Task #5 not found"

### Delete Task

**AC-011**: Deleting existing task
- **Given** tasks #1, #2, #3 exist
- **When** user deletes task #2
- **Then** task #2 no longer appears in View Tasks, and tasks #1 and #3 retain their original IDs

**AC-012**: Deleting non-existent task
- **Given** tasks #1 and #2 exist
- **When** user attempts to delete task #99
- **Then** system displays "Error: Task #99 not found" and no tasks are deleted

**AC-013**: ID permanence after deletion
- **Given** tasks #1, #2, #3 exist and task #2 is deleted
- **When** user adds a new task
- **Then** new task receives ID=4 (not ID=2)

### Mark Complete/Incomplete

**AC-014**: Marking incomplete task as complete
- **Given** task #1 exists with status incomplete (✗)
- **When** user selects "Mark Task Complete" and enters ID=1
- **Then** task #1 status changes to complete (✓) and displays "Task #1 marked as complete"

**AC-015**: Marking complete task as incomplete
- **Given** task #1 exists with status complete (✓)
- **When** user selects "Mark Task Incomplete" and enters ID=1
- **Then** task #1 status changes to incomplete (✗) and displays "Task #1 marked as incomplete"

**AC-016**: Marking non-existent task
- **Given** no tasks exist
- **When** user attempts to mark task #1 as complete
- **Then** system displays "Error: Task #1 not found"

### Exit

**AC-017**: Graceful exit
- **Given** application is running
- **When** user selects "Exit"
- **Then** system displays "Goodbye!" and program terminates without errors

## Out of Scope (Phase I)

The following are explicitly **NOT** included in this specification:

- **Persistence**: Tasks are lost when program exits (no file I/O or database)
- **Task Filtering**: No search, filter by status, or sort by date features
- **Task Prioritization**: No priority levels (high/medium/low)
- **Task Deadlines**: No due dates or reminders
- **Task Categories**: No tags, labels, or project grouping
- **Undo/Redo**: No operation history or reversal
- **Bulk Operations**: No delete all, mark all complete, or batch updates
- **Import/Export**: No CSV, JSON, or other format support
- **Multi-User**: Single-user only, no authentication or permissions
- **Colorized Output**: Optional (ANSI colors may be added if trivial, but not required)
- **Command-Line Arguments**: No CLI flags or non-interactive mode
- **Configuration**: No settings file or customization options

## Non-Functional Requirements

### Performance

- **NFR-001**: All operations (add, view, update, delete, mark) MUST complete in <100ms for up to 100 tasks
- **NFR-002**: Application startup MUST complete in <500ms
- **NFR-003**: Memory usage MUST remain stable during 50+ consecutive operations (no leaks)

### Usability

- **NFR-004**: Error messages MUST be understandable by non-technical users
- **NFR-005**: Menu options MUST be numbered for easy selection
- **NFR-006**: Task display MUST be readable on standard 80-column terminal

### Reliability

- **NFR-007**: Application MUST handle invalid inputs without crashing
- **NFR-008**: Application MUST not enter unrecoverable states (always return to main menu)

### Maintainability

- **NFR-009**: All functions MUST have type hints (Python 3.13+)
- **NFR-010**: All public functions MUST have Google-style docstrings
- **NFR-011**: Code MUST adhere to constitutional limits (25 lines/function, 7 methods/class)

## Constitutional Compliance

This specification adheres to the following constitutional principles:

- **Principle I (Spec-Driven Development)**: This spec defines all functionality; no code will be written manually
- **Principle II (Clean Architecture)**: Domain (Task), Application (Use Cases), Interface (CLI) layers separated
- **Principle III (Single Responsibility)**: Each operation is a distinct use case with single purpose
- **Principle IV (Test-First Development)**: Acceptance criteria provide test specifications for TDD
- **Principle V (Deterministic Behavior)**: IDs auto-increment predictably, operations produce consistent output
- **Principle VI (Defensive Input Handling)**: All inputs validated with explicit error messages
- **Principle VII (Simplicity and YAGNI)**: Only specified features included; no speculation on future needs

## Appendix: Example Session

```
=================================
    TODO APPLICATION
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=================================
Enter your choice (1-7): 1

Enter task title: Buy groceries
Enter task description: Milk, eggs, bread
Task #1 added successfully

=================================
    TODO APPLICATION
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=================================
Enter your choice (1-7): 1

Enter task title: Write report
Enter task description: Q4 financial summary
Task #2 added successfully

=================================
    TODO APPLICATION
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=================================
Enter your choice (1-7): 2

[1] Buy groceries | Milk, eggs, bread | ✗

[2] Write report | Q4 financial summary | ✗

=================================
    TODO APPLICATION
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=================================
Enter your choice (1-7): 5

Enter task ID: 1
Task #1 marked as complete

=================================
    TODO APPLICATION
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=================================
Enter your choice (1-7): 2

[1] Buy groceries | Milk, eggs, bread | ✓

[2] Write report | Q4 financial summary | ✗

=================================
    TODO APPLICATION
=================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
=================================
Enter your choice (1-7): 7

Goodbye!
```

---

**Specification Version**: 1.0.0
**Last Updated**: 2026-01-08
**Reviewers**: [Pending]
**Approval Status**: Awaiting Review
