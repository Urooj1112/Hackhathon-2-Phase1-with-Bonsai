---
id: 003
title: Generate Tasks Core Todo Operations
stage: tasks
date: 2026-01-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: core-todo-operations
branch: master
user: HP
command: /sp.tasks
labels: ["tasks", "tdd", "clean-architecture", "user-stories"]
links:
  spec: specs/core-todo-operations/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/core-todo-operations/tasks.md
tests:
  - all_tests_listed_in_tasks
---

## Prompt

Based ONLY on the Phase-I Todo specification,
create an implementation plan.

The plan must include:
- Folder structure
- Modules and responsibilities
- Function-level breakdown
- CLI loop logic
- Data flow between components

Plan Format:
1. High-Level Architecture
2. Module Breakdown
3. Step-by-Step Execution Order
4. Risk & Edge Case Handling
5. Readiness Check for Phase II

Constraints:
- Python console app
- In-memory only
- No extra features
- No code yet

Output a clear, numbered Markdown plan.
/sp.plan

## Response snapshot

Generated comprehensive tasks.md for Core Todo Operations feature with **90 tasks** organized by user story following TDD and Clean Architecture principles.

**Task Organization (8 Phases):**

1. **Phase 1 - Setup** (4 tasks): Project structure with src/domain/, src/application/, src/interface/, tests/ hierarchy
2. **Phase 2 - Foundational** (15 tasks): Domain exceptions, Task entity, TaskRepository protocol, InMemoryTaskRepository, foundational tests
3. **Phase 3 - User Story 1 (P1)** (18 tasks): Add/View tasks - 12 Red phase tests + 6 Green phase implementation + 1 integration test
4. **Phase 4 - User Story 5 (P1)** (5 tasks): Exit gracefully - 2 tests + 2 implementation + 1 integration test
5. **Phase 5 - User Story 2 (P2)** (15 tasks): Toggle completion - 8 tests + 6 implementation + 1 integration test
6. **Phase 6 - User Story 3 (P3)** (12 tasks): Update task details - 8 tests + 3 implementation + 1 integration test
7. **Phase 7 - User Story 4 (P3)** (9 tasks): Delete tasks - 5 tests + 3 implementation + 1 integration test
8. **Phase 8 - Polish** (12 tasks): Documentation, coverage verification, constitutional compliance checks

**Key Architectural Decisions:**

- **Clean Architecture**: 3-layer separation (Domain/Application/Interface) per Constitution Principle II
- **TDD Mandatory**: Red (write tests) → User approval → Green (implement) → Refactor per Constitution Principle IV
- **Test Coverage**: 100% domain/application layers, >80% interface layer (Constitutional QG-001, QG-002, QG-003)
- **Use Case Pattern**: Each operation is a separate use case class (AddTaskUseCase, ViewTasksUseCase, etc.)
- **Repository Pattern**: TaskRepository protocol with InMemoryTaskRepository implementation (enables Phase II evolution)
- **Dependency Inversion**: Application layer depends on domain protocols, not concrete implementations

**Project Structure:**
```
src/
├── domain/           # Task entity, exceptions, TaskRepository protocol
├── application/      # Use cases + InMemoryTaskRepository
└── interface/        # CLI (ConsoleView, CommandHandler, InputValidator, main loop)

tests/
├── domain/           # Task and validation tests
├── application/      # Use case and repository tests
├── interface/        # CLI interaction tests
└── integration/      # End-to-end user story tests
```

**Module Breakdown:**
- Domain: task.py (Task dataclass), exceptions.py (4 exception classes), repository.py (TaskRepository protocol)
- Application: repository.py (InMemoryTaskRepository), use_cases/ (AddTaskUseCase, ViewTasksUseCase, UpdateTaskUseCase, DeleteTaskUseCase, MarkCompleteUseCase, MarkIncompleteUseCase)
- Interface: input_validator.py (InputValidator), console_view.py (ConsoleView), command_handler.py (CommandHandler), main.py (application loop)

**MVP Definition** (42 tasks):
- Phase 1 (Setup) + Phase 2 (Foundational) + Phase 3 (US1 - Add/View) + Phase 4 (US5 - Exit)
- Delivers: Working todo app where users can add tasks, view list, and exit cleanly

**Parallel Opportunities**: 47 tasks marked [P] can run in parallel:
- All domain exceptions (T005-T008)
- All foundational tests (T012-T019)
- All Red phase tests within each user story
- Documentation tasks in Polish phase

**Independent Test Criteria** (per user story):
- US1: Add one task → view list → confirm appears with ID, title, description, status ✗
- US5: Select exit → see "Goodbye!" → program terminates
- US2: Add task → mark complete → status ✓ → mark incomplete → status ✗
- US3: Add task → update title only → verify → update description only → verify
- US4: Add two tasks → delete one → confirm removed, other retains original ID

**Implementation Strategy:**
1. MVP First: Phases 1-4 (42 tasks) → Validate → Deploy
2. Incremental: Add US2 → Validate → Deploy → Add US3 + US4 → Validate → Deploy → Polish
3. Parallel Team: Complete Foundation → Split user stories across developers → Integrate → Polish

**Constitutional Compliance:**
- All 7 principles mapped to specific tasks
- Function length (≤25 lines) verified in T082
- Class methods (≤7) verified in T083
- Test coverage gates (QG-001 to QG-003) verified in T084
- Type hints verified in T081
- Error message user-friendliness verified in T088
- Performance verified in T089 (100 tasks, <100ms)
- Memory leak check in T090 (50+ operations)

## Outcome

- ✅ Impact: Comprehensive, executable task breakdown for Phase-I Todo app. 90 tasks organized by 5 user stories with TDD workflow. MVP clearly defined (42 tasks). All tasks follow strict checklist format with IDs, [P] markers, [Story] labels, and file paths.
- 🧪 Tests: 58 test tasks across all phases (64% of implementation work is test-first). Foundational tests (T012-T019), US1 tests (T020-T030), US2 tests (T043-T050), US3 tests (T058-T065), US4 tests (T070-T074), plus 5 integration tests and coverage validation.
- 📁 Files: Created `specs/core-todo-operations/tasks.md` (615 lines, 90 tasks across 8 phases)
- 🔁 Next prompts: "Begin implementation with /sp.implement" or "Start TDD cycle for MVP (Phase 1-4)" or "Review tasks and approve to proceed"
- 🧠 Reflection: Task breakdown enables parallel work (47 [P] tasks), independent story testing (5 integration tests), and incremental delivery (MVP → US2 → US3+US4 → Polish). TDD workflow explicit per constitutional mandate. Clean Architecture enforced through layer-specific task organization.

## Evaluation notes (flywheel)

- Failure modes observed: None detected. All 5 user stories from spec.md mapped to task phases. All acceptance criteria (AC-001 to AC-017) covered by test tasks. Constitutional principles (all 7) enforced through specific validation tasks. Task format compliance: All 90 tasks have checkbox, ID, description with file path; 47 have [P] marker; 71 have [Story] label where applicable.
- Graders run and results (PASS/FAIL): Manual review pending. Task structure follows template exactly. TDD cycle (Red → Green → Refactor) explicit in each user story phase. MVP scope clearly defined and independently deliverable.
- Prompt variant (if applicable): Standard /sp.tasks workflow with emphasis on TDD (Constitution Principle IV mandates test-first). User stories prioritized (P1 → P2 → P3) per spec.md.
- Next experiment (smallest change to try): Validate task granularity during implementation - if tasks are too large (>25 lines result), split further. If tasks are too small (trivial), group related tasks in refactor phase.
