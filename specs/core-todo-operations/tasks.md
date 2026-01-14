---
description: "Task list for Core Todo Operations feature implementation"
---

# Tasks: Core Todo Operations

**Input**: Design documents from `/specs/core-todo-operations/`
**Prerequisites**: spec.md (user stories with priorities)

**Tests**: Test-First Development is NON-NEGOTIABLE per Constitution Principle IV. All test tasks MUST be completed BEFORE implementation tasks.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

**Project Structure** (Clean Architecture):
```
src/
├── domain/           # Domain layer (Task entity, exceptions, protocols)
├── application/      # Application layer (use cases)
└── interface/        # Interface layer (CLI, input/output)

tests/
├── domain/           # Domain layer tests
├── application/      # Application layer tests
├── interface/        # Interface layer tests
└── integration/      # End-to-end integration tests
```

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure following Clean Architecture

- [ ] T001 Create project directory structure: src/domain/, src/application/, src/interface/, tests/domain/, tests/application/, tests/interface/, tests/integration/
- [ ] T002 Create src/__init__.py and subdirectory __init__.py files to establish Python package structure
- [ ] T003 Create requirements.txt (empty - no external dependencies per constitution)
- [ ] T004 Create README.md with project description and execution instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core domain infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Domain Layer Foundation

- [ ] T005 [P] Create TodoAppError base exception class in src/domain/exceptions.py
- [ ] T006 [P] Create InvalidTaskError exception in src/domain/exceptions.py
- [ ] T007 [P] Create TaskNotFoundError exception in src/domain/exceptions.py
- [ ] T008 [P] Create InvalidCommandError exception in src/domain/exceptions.py
- [ ] T009 Create TaskRepository protocol (abstract interface) in src/domain/repository.py with methods: add(), get_by_id(), get_all(), update(), delete(), mark_complete(), mark_incomplete()
- [ ] T010 Create Task dataclass in src/domain/task.py with fields: id (int), title (str), description (str), completed (bool); add validation methods for title and description length/emptiness

### Application Layer Foundation

- [ ] T011 Create InMemoryTaskRepository implementation in src/application/repository.py implementing TaskRepository protocol with auto-incrementing ID logic (starting from 1, never reusing deleted IDs)

### Tests for Foundational Layer

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T012 [P] Write test_task_creation_with_valid_data in tests/domain/test_task.py
- [ ] T013 [P] Write test_task_title_validation_empty_title in tests/domain/test_task.py
- [ ] T014 [P] Write test_task_title_validation_exceeds_200_chars in tests/domain/test_task.py
- [ ] T015 [P] Write test_task_description_validation_exceeds_200_chars in tests/domain/test_task.py
- [ ] T016 [P] Write test_inmemory_repository_add_task in tests/application/test_repository.py
- [ ] T017 [P] Write test_inmemory_repository_get_by_id in tests/application/test_repository.py
- [ ] T018 [P] Write test_inmemory_repository_id_auto_increment in tests/application/test_repository.py
- [ ] T019 [P] Write test_inmemory_repository_id_not_reused_after_deletion in tests/application/test_repository.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and View First Task (Priority: P1) 🎯 MVP

**Goal**: User can add a task with title and description, then view all tasks in a formatted list

**Independent Test**: Launch app, add one task, view the list, confirm task appears with correct ID, title, description, and incomplete status (✗)

### Tests for User Story 1 - Red Phase (Write FIRST, ensure FAIL)

- [ ] T020 [P] [US1] Write test_add_task_use_case_with_valid_data in tests/application/test_add_task.py
- [ ] T021 [P] [US1] Write test_add_task_use_case_empty_title_raises_error in tests/application/test_add_task.py
- [ ] T022 [P] [US1] Write test_add_task_use_case_title_exceeds_limit_raises_error in tests/application/test_add_task.py
- [ ] T023 [P] [US1] Write test_add_task_use_case_description_exceeds_limit_raises_error in tests/application/test_add_task.py
- [ ] T024 [P] [US1] Write test_add_task_use_case_empty_description_accepted in tests/application/test_add_task.py
- [ ] T025 [P] [US1] Write test_view_tasks_use_case_empty_repository in tests/application/test_view_tasks.py
- [ ] T026 [P] [US1] Write test_view_tasks_use_case_multiple_tasks in tests/application/test_view_tasks.py
- [ ] T027 [P] [US1] Write test_cli_add_task_command_valid_input in tests/interface/test_cli.py
- [ ] T028 [P] [US1] Write test_cli_add_task_command_invalid_title in tests/interface/test_cli.py
- [ ] T029 [P] [US1] Write test_cli_view_tasks_command_no_tasks in tests/interface/test_cli.py
- [ ] T030 [P] [US1] Write test_cli_view_tasks_command_with_tasks in tests/interface/test_cli.py

### Implementation for User Story 1 - Green Phase

- [ ] T031 [US1] Implement AddTaskUseCase class in src/application/use_cases/add_task.py with execute(title: str, description: str) method that validates inputs and calls repository.add()
- [ ] T032 [US1] Implement ViewTasksUseCase class in src/application/use_cases/view_tasks.py with execute() method that calls repository.get_all() and returns task list
- [ ] T033 [US1] Implement InputValidator class in src/interface/input_validator.py with methods: validate_title(), validate_description(), validate_task_id()
- [ ] T034 [US1] Implement ConsoleView class in src/interface/console_view.py with methods: display_menu(), display_task_list(), display_message(), display_error(), prompt_for_input()
- [ ] T035 [US1] Implement CommandHandler class in src/interface/command_handler.py with handle_add_task() and handle_view_tasks() methods that coordinate InputValidator, use cases, and ConsoleView
- [ ] T036 [US1] Create main application loop in src/interface/main.py with menu display, command dispatch to CommandHandler, and exit handling

### Integration Test for User Story 1

- [ ] T037 [US1] Write integration test test_add_and_view_task_end_to_end in tests/integration/test_user_story_1.py that simulates full add→view workflow

**Checkpoint**: At this point, User Story 1 should be fully functional - user can add tasks and view them independently

---

## Phase 4: User Story 5 - Exit Application Gracefully (Priority: P1)

**Goal**: User can cleanly exit the application from the main menu

**Independent Test**: Launch app, select Exit option, confirm "Goodbye!" message displays and program terminates without errors

### Tests for User Story 5 - Red Phase

- [ ] T038 [P] [US5] Write test_cli_exit_command_displays_goodbye in tests/interface/test_cli.py
- [ ] T039 [P] [US5] Write test_cli_exit_command_terminates_loop in tests/interface/test_cli.py

### Implementation for User Story 5 - Green Phase

- [ ] T040 [US5] Add handle_exit() method to CommandHandler in src/interface/command_handler.py that displays "Goodbye!" via ConsoleView and returns exit flag
- [ ] T041 [US5] Update main loop in src/interface/main.py to handle exit command and break loop on exit flag

### Integration Test for User Story 5

- [ ] T042 [US5] Write integration test test_exit_application_gracefully in tests/integration/test_user_story_5.py

**Checkpoint**: MVP is now complete (User Story 1 + User Story 5) - fully functional add/view/exit todo app

---

## Phase 5: User Story 2 - Toggle Task Completion (Priority: P2)

**Goal**: User can mark tasks as complete (✓) or incomplete (✗) by task ID

**Independent Test**: Add one task, mark it complete, verify status changes to ✓, mark it incomplete, verify status reverts to ✗

### Tests for User Story 2 - Red Phase

- [ ] T043 [P] [US2] Write test_mark_complete_use_case_existing_task in tests/application/test_mark_complete.py
- [ ] T044 [P] [US2] Write test_mark_complete_use_case_nonexistent_task_raises_error in tests/application/test_mark_complete.py
- [ ] T045 [P] [US2] Write test_mark_incomplete_use_case_existing_task in tests/application/test_mark_incomplete.py
- [ ] T046 [P] [US2] Write test_mark_incomplete_use_case_nonexistent_task_raises_error in tests/application/test_mark_incomplete.py
- [ ] T047 [P] [US2] Write test_cli_mark_complete_command_valid_id in tests/interface/test_cli.py
- [ ] T048 [P] [US2] Write test_cli_mark_complete_command_invalid_id in tests/interface/test_cli.py
- [ ] T049 [P] [US2] Write test_cli_mark_incomplete_command_valid_id in tests/interface/test_cli.py
- [ ] T050 [P] [US2] Write test_view_tasks_displays_completion_status_symbols in tests/application/test_view_tasks.py

### Implementation for User Story 2 - Green Phase

- [ ] T051 [US2] Implement MarkCompleteUseCase class in src/application/use_cases/mark_complete.py with execute(task_id: int) method
- [ ] T052 [US2] Implement MarkIncompleteUseCase class in src/application/use_cases/mark_incomplete.py with execute(task_id: int) method
- [ ] T053 [US2] Add handle_mark_complete() method to CommandHandler in src/interface/command_handler.py
- [ ] T054 [US2] Add handle_mark_incomplete() method to CommandHandler in src/interface/command_handler.py
- [ ] T055 [US2] Update ConsoleView.display_task_list() in src/interface/console_view.py to display ✓ for completed tasks and ✗ for incomplete tasks
- [ ] T056 [US2] Update main menu in src/interface/main.py to include options 5 (Mark Complete) and 6 (Mark Incomplete)

### Integration Test for User Story 2

- [ ] T057 [US2] Write integration test test_toggle_task_completion_end_to_end in tests/integration/test_user_story_2.py that adds task, marks complete, marks incomplete

**Checkpoint**: User Story 2 complete - users can now track task completion status

---

## Phase 6: User Story 3 - Update Task Details (Priority: P3)

**Goal**: User can update task title and/or description by task ID without deleting and recreating

**Independent Test**: Add one task, update title only, verify change; update description only, verify change; confirm both fields can be updated simultaneously

### Tests for User Story 3 - Red Phase

- [ ] T058 [P] [US3] Write test_update_task_use_case_update_title_only in tests/application/test_update_task.py
- [ ] T059 [P] [US3] Write test_update_task_use_case_update_description_only in tests/application/test_update_task.py
- [ ] T060 [P] [US3] Write test_update_task_use_case_update_both_fields in tests/application/test_update_task.py
- [ ] T061 [P] [US3] Write test_update_task_use_case_nonexistent_task_raises_error in tests/application/test_update_task.py
- [ ] T062 [P] [US3] Write test_update_task_use_case_invalid_title_raises_error in tests/application/test_update_task.py
- [ ] T063 [P] [US3] Write test_cli_update_task_command_title_only in tests/interface/test_cli.py
- [ ] T064 [P] [US3] Write test_cli_update_task_command_description_only in tests/interface/test_cli.py
- [ ] T065 [P] [US3] Write test_cli_update_task_command_both_fields in tests/interface/test_cli.py

### Implementation for User Story 3 - Green Phase

- [ ] T066 [US3] Implement UpdateTaskUseCase class in src/application/use_cases/update_task.py with execute(task_id: int, new_title: str | None, new_description: str | None) method
- [ ] T067 [US3] Add handle_update_task() method to CommandHandler in src/interface/command_handler.py that prompts for ID, new title (or Enter to keep), new description (or Enter to keep)
- [ ] T068 [US3] Update main menu in src/interface/main.py to include option 3 (Update Task)

### Integration Test for User Story 3

- [ ] T069 [US3] Write integration test test_update_task_details_end_to_end in tests/integration/test_user_story_3.py

**Checkpoint**: User Story 3 complete - users can now correct or refine task details

---

## Phase 7: User Story 4 - Delete Completed Tasks (Priority: P3)

**Goal**: User can remove tasks by ID to keep the task list focused

**Independent Test**: Add two tasks, delete one by ID, verify it no longer appears, confirm other task remains with original ID

### Tests for User Story 4 - Red Phase

- [ ] T070 [P] [US4] Write test_delete_task_use_case_existing_task in tests/application/test_delete_task.py
- [ ] T071 [P] [US4] Write test_delete_task_use_case_nonexistent_task_raises_error in tests/application/test_delete_task.py
- [ ] T072 [P] [US4] Write test_delete_task_preserves_other_task_ids in tests/application/test_delete_task.py
- [ ] T073 [P] [US4] Write test_cli_delete_task_command_valid_id in tests/interface/test_cli.py
- [ ] T074 [P] [US4] Write test_cli_delete_task_command_invalid_id in tests/interface/test_cli.py

### Implementation for User Story 4 - Green Phase

- [ ] T075 [US4] Implement DeleteTaskUseCase class in src/application/use_cases/delete_task.py with execute(task_id: int) method
- [ ] T076 [US4] Add handle_delete_task() method to CommandHandler in src/interface/command_handler.py
- [ ] T077 [US4] Update main menu in src/interface/main.py to include option 4 (Delete Task)

### Integration Test for User Story 4

- [ ] T078 [US4] Write integration test test_delete_task_end_to_end in tests/integration/test_user_story_4.py that adds multiple tasks, deletes one, confirms ID permanence

**Checkpoint**: All user stories complete - full feature set implemented

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and ensure constitutional compliance

- [ ] T079 [P] Add comprehensive module docstrings (Google style) to all src/ modules
- [ ] T080 [P] Add comprehensive function docstrings (Google style) with Args, Returns, Raises to all public functions
- [ ] T081 Verify all functions have type hints (Python 3.13+) and no `# type: ignore` comments exist
- [ ] T082 Verify all functions are ≤25 lines (excluding docstrings) per Constitution Principle III
- [ ] T083 Verify all classes have ≤7 methods (excluding `__init__`, `__repr__`) per Constitution Principle III
- [ ] T084 Run all tests and verify 100% coverage for domain and application layers, >80% for interface layer (per Constitution QG-001, QG-002, QG-003)
- [ ] T085 Create src/__main__.py entry point to enable `python -m src` execution
- [ ] T086 Update README.md with usage examples, architecture diagram, and constitutional compliance statement
- [ ] T087 [P] Add inline comments only where logic is non-obvious (per Constitution coding rules)
- [ ] T088 Verify error messages are user-friendly with no stack traces exposed to users (per FR-022)
- [ ] T089 Test application with 100 tasks to verify performance <100ms per operation (per NFR-001)
- [ ] T090 Test application with 50+ consecutive operations to verify no memory leaks (per NFR-003)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User Story 1 (P1) + User Story 5 (P1) = MVP (can be implemented first)
  - User Story 2 (P2), User Story 3 (P3), User Story 4 (P3) can proceed in priority order or in parallel
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1) - Add/View**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P1) - Exit**: Can start after US1 or in parallel with US1 (only needs main loop structure)
- **User Story 2 (P2) - Toggle Completion**: Can start after Foundational (Phase 2) - Independently testable but integrates with US1 (view displays status)
- **User Story 3 (P3) - Update**: Can start after Foundational (Phase 2) - Independently testable, no dependencies
- **User Story 4 (P3) - Delete**: Can start after Foundational (Phase 2) - Independently testable, tests ID permanence

### Within Each User Story (TDD Cycle)

1. **Red Phase**: Write all tests FIRST, ensure they FAIL (proves they test something)
2. **Green Phase**: Implement minimum code to pass tests
3. **Refactor Phase**: Improve code quality while keeping tests green
4. User approval required before moving Red → Green (per Constitution Principle IV)

### Parallel Opportunities

- **Phase 1 (Setup)**: All tasks can run in parallel
- **Phase 2 (Foundational)**: Tasks marked [P] can run in parallel within their sub-phase (all domain exceptions, all tests for foundational layer)
- **Phase 3-7 (User Stories)**:
  - Once Foundational phase completes, all user stories CAN start in parallel (if team capacity allows)
  - Within each story: All test tasks marked [P] can run in parallel
- **Phase 8 (Polish)**: Tasks marked [P] (documentation, coverage checks) can run in parallel

---

## Parallel Example: User Story 1 Red Phase

```bash
# Launch all test creation tasks for User Story 1 together:
T020: "Write test_add_task_use_case_with_valid_data in tests/application/test_add_task.py"
T021: "Write test_add_task_use_case_empty_title_raises_error in tests/application/test_add_task.py"
T022: "Write test_add_task_use_case_title_exceeds_limit_raises_error in tests/application/test_add_task.py"
T023: "Write test_add_task_use_case_description_exceeds_limit_raises_error in tests/application/test_add_task.py"
T024: "Write test_add_task_use_case_empty_description_accepted in tests/application/test_add_task.py"
T025: "Write test_view_tasks_use_case_empty_repository in tests/application/test_view_tasks.py"
T026: "Write test_view_tasks_use_case_multiple_tasks in tests/application/test_view_tasks.py"
T027: "Write test_cli_add_task_command_valid_input in tests/interface/test_cli.py"
T028: "Write test_cli_add_task_command_invalid_title in tests/interface/test_cli.py"
T029: "Write test_cli_view_tasks_command_no_tasks in tests/interface/test_cli.py"
T030: "Write test_cli_view_tasks_command_with_tasks in tests/interface/test_cli.py"
```

All 11 test tasks can be written simultaneously since they target different test files and test different behaviors.

---

## Implementation Strategy

### MVP First (User Story 1 + User Story 5 Only)

1. Complete **Phase 1: Setup** → Project structure ready
2. Complete **Phase 2: Foundational** → Domain and repository infrastructure ready
3. Complete **Phase 3: User Story 1** (Red → Green → Refactor) → Add and view tasks working
4. Complete **Phase 4: User Story 5** → Exit functionality working
5. **STOP and VALIDATE**: Test MVP independently (can add tasks, view them, exit cleanly)
6. Deploy/demo MVP if ready

**MVP delivers**: A working todo app where users can add tasks, see their list, and exit - the core value proposition

### Incremental Delivery (Priority Order)

1. Complete Setup + Foundational → Foundation ready
2. Add **User Story 1** + **User Story 5** → Test independently → **Deploy/Demo MVP**
3. Add **User Story 2** (Toggle Completion) → Test independently → Deploy/Demo
4. Add **User Story 3** (Update) → Test independently → Deploy/Demo
5. Add **User Story 4** (Delete) → Test independently → Deploy/Demo
6. Complete **Phase 8: Polish** → Final quality checks and documentation
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. **Together**: Complete Setup (Phase 1) + Foundational (Phase 2)
2. **Once Foundational is done, split work**:
   - Developer A: User Story 1 (Add/View) + User Story 5 (Exit) → MVP
   - Developer B: User Story 2 (Toggle Completion)
   - Developer C: User Story 3 (Update) + User Story 4 (Delete)
3. Stories complete and integrate independently
4. **Together**: Phase 8 (Polish & Cross-Cutting)

---

## Constitutional Compliance Checklist

Before marking feature complete, verify:

- [ ] **Principle I (Spec-Driven)**: All code traceable to spec.md acceptance criteria
- [ ] **Principle II (Clean Architecture)**: Domain/Application/Interface layers properly separated with zero domain dependencies on outer layers
- [ ] **Principle III (SRP)**: All functions ≤25 lines, all classes ≤7 methods
- [ ] **Principle IV (Test-First)**: All tests written before implementation, 100% domain/application coverage, >80% interface coverage
- [ ] **Principle V (Deterministic)**: IDs auto-increment from 1, deleted IDs never reused, operations produce consistent output
- [ ] **Principle VI (Defensive Input)**: All inputs validated, error messages start with "Error: ", no stack traces exposed
- [ ] **Principle VII (Simplicity)**: No features beyond spec, no premature abstractions, no external dependencies

---

## Notes

- **[P] tasks** = different files, no dependencies - can run in parallel
- **[Story] label** = maps task to specific user story for traceability and independent testing
- **TDD is mandatory**: Red (tests fail) → User approval → Green (tests pass) → Refactor
- Each user story should be independently completable and testable
- Verify tests FAIL before implementing (proves they test something)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- **No external dependencies** - Python 3.13+ standard library only
- **No persistence** - all data in memory (lost on exit)
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Summary

**Total Tasks**: 90
- Phase 1 (Setup): 4 tasks
- Phase 2 (Foundational): 15 tasks (5 implementation + 8 tests + 2 infrastructure)
- Phase 3 (US1 - Add/View): 18 tasks (12 tests + 6 implementation + 1 integration)
- Phase 4 (US5 - Exit): 5 tasks (2 tests + 2 implementation + 1 integration)
- Phase 5 (US2 - Toggle): 15 tasks (8 tests + 6 implementation + 1 integration)
- Phase 6 (US3 - Update): 12 tasks (8 tests + 3 implementation + 1 integration)
- Phase 7 (US4 - Delete): 9 tasks (5 tests + 3 implementation + 1 integration)
- Phase 8 (Polish): 12 tasks

**MVP Scope** (Minimum to deliver value): Phase 1 + Phase 2 + Phase 3 + Phase 4 = 42 tasks

**Parallel Opportunities**: 47 tasks marked [P] can run in parallel when dependencies are met

**Independent Test Criteria**:
- US1: Add task + view list = functional todo app
- US5: Exit displays "Goodbye!" and terminates
- US2: Toggle completion changes status symbols
- US3: Update modifies fields without deletion
- US4: Delete removes task, IDs remain stable

**Suggested First Implementation**: MVP (US1 + US5) → Deploy → US2 → Deploy → US3 + US4 → Deploy → Polish
