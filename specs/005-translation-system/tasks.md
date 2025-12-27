# Implementation Tasks: Translation System (English ↔ Urdu)

**Feature**: Translation System (English ↔ Urdu) | **Branch**: `005-translation-system`
**Created**: 2025-12-27 | **Spec**: [link to spec.md](./spec.md) | **Plan**: [link to plan.md](./plan.md)

**Input**: Design documents from `/specs/005-translation-system/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Constitution Compliance Check

### Phase Isolation Check
- [X] Only current phase tasks are included
- [X] No future phase tasks are included
- [X] Previous phase is locked before starting current phase tasks

### No Scope Creep Check
- [X] Tasks belong only to their assigned phase
- [X] No "small additions" from future phases
- [X] No refactors after phase lock

### AI-Friendly Structure Check
- [X] Clear specs before planning
- [X] Clear plans before implementation
- [X] Clear verification before locking

### Deterministic Execution Check
- [X] Every phase produces verifiable outputs
- [X] Ambiguity is resolved in Specify, not Implement

### Mandatory Phase Execution Lifecycle Check
- [X] Follows Specify → Plan → Implement → Verify → Lock sequence
- [X] No phase overlap allowed

### Locked Project Phases Check
- [X] Project phases completed in locked order
- [X] No skipping phases

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 [P] Create docusaurus/src/components directory
- [ ] T002 [P] Create docusaurus/src/services directory
- [ ] T003 [P] Create docusaurus/src/css directory
- [ ] T004 [P] Create backend/src/services directory
- [ ] T005 [P] Create backend/src/api directory
- [ ] T006 [P] Create backend/src/models directory
- [ ] T007 [P] Create agents/claude-subagents directory
- [ ] T008 [P] Create agents/claude-subagents/agent-skills directory

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T009 [P] Create TranslationSession model in backend/src/models/translation.py
- [X] T010 [P] Create TranslatedContent model in backend/src/models/translation.py
- [X] T011 [P] Setup API routing and middleware structure in backend/src/api/translation.py
- [X] T012 [P] Create Claude Code Subagent base framework in agents/claude-subagents/base_agent.py
- [X] T013 [P] Create Agent Skills base framework in agents/claude-subagents/agent-skills/base_skill.py
- [X] T014 [P] Setup environment configuration management for Claude API in backend/src/config/translation.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Translate Chapter Content (Priority: P1) 🎯 MVP

**Goal**: Enable authenticated users to translate book content between English and Urdu while preserving technical accuracy

**Independent Test**: Can be fully tested by logging in with a user account, navigating to a chapter, clicking the "Translate to Urdu" button, and verifying that the content is accurately translated while preserving technical terms and code blocks.

### Implementation for User Story 1

- [X] T015 [P] [US1] Create TranslationToggle component in docusaurus/src/components/TranslationToggle.js
- [X] T016 [P] [US1] Create TranslatedContent component in docusaurus/src/components/TranslatedContent.js
- [X] T017 [US1] Implement translation service in docusaurus/src/services/translation.js
- [X] T018 [US1] Implement translation API endpoint in backend/src/api/translation.py
- [X] T019 [US1] Implement translation service in backend/src/services/translation.py
- [X] T020 [US1] Create TranslationAgent in agents/claude-subagents/translation-agent.py
- [X] T021 [US1] Create TechnicalTermPreservation skill in agents/claude-subagents/agent-skills/term-preservation.py
- [X] T022 [US1] Create CodeBlockProtection skill in agents/claude-subagents/agent-skills/code-protection.py
- [X] T023 [US1] Integrate translation into DocPage in docusaurus/src/pages/DocPage.js
- [X] T024 [US1] Add visual distinction styling for translated content in docusaurus/src/css/translation.css

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Translated Content with Preserved Elements (Priority: P1)

**Goal**: Ensure translated content displays with preserved code blocks and formatting so that technical information remains accurate and usable

**Independent Test**: Can be fully tested by translating content with code blocks and verifying that the code remains unchanged and properly formatted.

### Implementation for User Story 2

- [X] T025 [P] [US2] Enhance TranslatedContent component with code block preservation in docusaurus/src/components/TranslatedContent.js
- [X] T026 [US2] Implement formatting preservation in translation service in docusaurus/src/services/translation.js
- [X] T027 [US2] Update translation API to include formatting metadata in backend/src/api/translation.py
- [X] T028 [US2] Enhance TranslationAgent with formatting maintenance in agents/claude-subagents/translation-agent.py
- [X] T029 [US2] Create FormattingMaintenance skill in agents/claude-subagents/agent-skills/formatting-maintenance.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Access Translation Controls (Priority: P2)

**Goal**: Ensure the "Translate to Urdu" button is only visible when the user is logged in

**Independent Test**: Can be fully tested by checking the visibility of the translation button when logged in versus when logged out.

### Implementation for User Story 3

- [X] T030 [P] [US3] Update TranslationToggle to check authentication state in docusaurus/src/components/TranslationToggle.js
- [X] T031 [US3] Implement button disable functionality when translation is active in docusaurus/src/components/TranslationToggle.js
- [X] T032 [US3] Add JWT authentication validation to translation endpoint in backend/src/api/translation.py
- [X] T033 [US3] Update translation service to verify user authentication in backend/src/services/translation.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T034 [P] Documentation updates in docs/translation.md
- [X] T035 Code cleanup and refactoring
- [ ] T036 Performance optimization for translation generation
- [ ] T037 Security hardening for API endpoints
- [X] T038 Run quickstart.md validation
- [X] T039 Add error handling for Claude Code Subagent unavailability
- [ ] T040 Add rate limiting to translation endpoints
- [ ] T041 Add caching for translated content to improve performance

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence