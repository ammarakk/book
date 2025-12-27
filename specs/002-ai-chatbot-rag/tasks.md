---

description: "Task list for Phase 2 – AI Chatbot (RAG System)"

---

# Tasks: Phase 2 – AI Chatbot (RAG System)

**Input**: Design documents from `/specs/002-ai-chatbot-rag/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Constitution Compliance Check

### Phase Isolation Check
- [ ] Only current phase tasks are included
- [ ] No future phase tasks are included
- [ ] Previous phase is locked before starting current phase tasks

### No Scope Creep Check
- [ ] Tasks belong only to their assigned phase
- [ ] No "small additions" from future phases
- [ ] No refactors after phase lock

### AI-Friendly Structure Check
- [ ] Clear specs before planning
- [ ] Clear plans before implementation
- [ ] Clear verification before locking

### Deterministic Execution Check
- [ ] Every phase produces verifiable outputs
- [ ] Ambiguity is resolved in Specify, not Implement

### Mandatory Phase Execution Lifecycle Check
- [ ] Follows Specify → Plan → Implement → Verify → Lock sequence
- [ ] No phase overlap allowed

### Locked Project Phases Check
- [ ] Project phases completed in locked order
- [ ] No skipping phases

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/`, `backend/src/`, `backend/tests/`
- **Frontend**: `docusaurus/physical-ai-book/`, `docusaurus/physical-ai-book/src/`, `docusaurus/physical-ai-book/tests/`
- Paths shown below assume the project structure from plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create backend directory structure in backend/
- [ ] T002 Create requirements.txt with FastAPI, Ollama, Qdrant, Neon dependencies
- [ ] T003 [P] Create main.py entry point in backend/main.py
- [ ] T004 Create config.py for environment variables in backend/config.py
- [ ] T005 Create frontend directory structure in docusaurus/physical-ai-book/
- [ ] T006 Initialize package.json for the Docusaurus project

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Setup Qdrant Cloud collection for book embeddings
- [ ] T008 Create Neon PostgreSQL schema for document metadata
- [ ] T009 [P] Create database models in backend/models/database.py
- [ ] T010 [P] Create embedding models in backend/models/embeddings.py
- [ ] T011 [P] Create chat models in backend/models/chat.py
- [ ] T012 Create document service in backend/services/document_service.py
- [ ] T013 Create embedding service in backend/services/embedding_service.py
- [ ] T014 Create RAG service in backend/services/rag_service.py
- [ ] T015 Create chat service in backend/services/chat_service.py
- [ ] T016 Create API routes for health check in backend/api/routes/health.py
- [ ] T017 Create API routes for chat in backend/api/routes/chat.py
- [ ] T018 Create dependency injection utilities in backend/api/deps.py
- [ ] T019 Create utility functions in backend/utils/helpers.py
- [ ] T020 Create validator functions in backend/utils/validators.py
- [ ] T021 Create ChatWidget component directory in docusaurus/physical-ai-book/src/components/ChatWidget/
- [ ] T022 Create FloatingButton.jsx component in docusaurus/physical-ai-book/src/components/ChatWidget/
- [ ] T023 Create ChatWindow.jsx component in docusaurus/physical-ai-book/src/components/ChatWidget/
- [ ] T024 Create ChatMessage.jsx component in docusaurus/physical-ai-book/src/components/ChatWidget/
- [ ] T025 Create ChatInput.jsx component in docusaurus/physical-ai-book/src/components/ChatWidget/
- [ ] T026 Create chat-widget.css in docusaurus/physical-ai-book/src/css/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Chatbot Interaction (Priority: P1) 🎯 MVP

**Goal**: Enable students to ask questions about the Physical AI & Humanoid Robotics book content and receive accurate answers based on the book's information.

**Independent Test**: Can be fully tested by verifying users can ask questions and receive accurate answers that are grounded in the book content.

### Implementation for User Story 1

- [ ] T027 [P] [US1] Implement POST /chat endpoint in backend/api/routes/chat.py
- [ ] T028 [P] [US1] Create ChatRequest model in backend/models/chat.py
- [ ] T029 [US1] Implement RAG pipeline in backend/services/rag_service.py
- [ ] T030 [US1] Implement Ollama integration in backend/services/rag_service.py
- [ ] T031 [US1] Create ChatResponse model in backend/models/chat.py
- [ ] T032 [US1] Implement chat session management in backend/services/chat_service.py
- [ ] T033 [US1] Create chat history functionality in backend/services/chat_service.py
- [ ] T034 [US1] Implement content grounding validation in backend/services/rag_service.py
- [ ] T035 [US1] Create error handling for missing context in backend/services/rag_service.py
- [ ] T036 [US1] Integrate ChatWidget with backend API in docusaurus/physical-ai-book/src/components/ChatWidget/ChatWindow.jsx
- [ ] T037 [US1] Implement message display in docusaurus/physical-ai-book/src/components/ChatWidget/ChatMessage.jsx
- [ ] T038 [US1] Implement question input in docusaurus/physical-ai-book/src/components/ChatWidget/ChatInput.jsx
- [ ] T039 [US1] Add Neon robotic theme styling to chat components in docusaurus/physical-ai-book/src/css/chat-widget.css
- [ ] T040 [US1] Test chat functionality with sample questions

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Context Selection Mode (Priority: P1)

**Goal**: Enable students to ask questions about specific text they have selected in the book and receive answers only based on that selected text.

**Independent Test**: Can be fully tested by verifying users can select text and ask questions that are answered only from the selected content.

### Implementation for User Story 2

- [ ] T041 [P] [US2] Implement POST /chat/selection endpoint in backend/api/routes/chat.py
- [ ] T042 [P] [US2] Create SelectionChatRequest model in backend/models/chat.py
- [ ] T043 [US2] Modify RAG pipeline for selected-text-only mode in backend/services/rag_service.py
- [ ] T044 [US2] Implement text selection capture in docusaurus/physical-ai-book/src/components/ChatWidget/ChatInput.jsx
- [ ] T045 [US2] Add selected-text-only answering logic in backend/services/rag_service.py
- [ ] T046 [US2] Implement hard-fail mechanism when answer not found in selection mode in backend/services/rag_service.py
- [ ] T047 [US2] Create selection mode UI in docusaurus/physical-ai-book/src/components/ChatWidget/ChatWindow.jsx
- [ ] T048 [US2] Test selection-only answering functionality

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Chatbot UI Integration (Priority: P2)

**Goal**: Provide students with easy access to the chatbot while reading the book without disrupting their reading experience.

**Independent Test**: Can be fully tested by verifying the chatbot icon is visible, animated, and the chat panel opens without disrupting the reading experience.

### Implementation for User Story 3

- [ ] T049 [P] [US3] Implement floating chatbot button animation in docusaurus/physical-ai-book/src/components/ChatWidget/FloatingButton.jsx
- [ ] T050 [P] [US3] Create robot-themed icon for chatbot in docusaurus/physical-ai-book/src/components/ChatWidget/FloatingButton.jsx
- [ ] T051 [US3] Implement smooth open/close animation for chat window in docusaurus/physical-ai-book/src/components/ChatWidget/ChatWindow.jsx
- [ ] T052 [US3] Integrate FloatingButton with ChatWindow in docusaurus/physical-ai-book/src/components/ChatWidget/
- [ ] T053 [US3] Add Neon robotic styling to FloatingButton in docusaurus/physical-ai-book/src/css/chat-widget.css
- [ ] T054 [US3] Ensure chat interface doesn't disrupt reading experience in docusaurus/physical-ai-book/src/components/ChatWidget/
- [ ] T055 [US3] Test UI integration with Docusaurus book layout
- [ ] T056 [US3] Add hover/idle animations to chatbot icon in docusaurus/physical-ai-book/src/components/ChatWidget/FloatingButton.jsx

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T057 [P] Add environment variable template (.env.example) in backend/
- [ ] T058 [P] Add comprehensive error handling across all endpoints in backend/api/routes/chat.py
- [ ] T059 [P] Implement caching layer for embeddings in backend/services/embedding_service.py
- [ ] T060 [P] Add logging functionality in backend/utils/helpers.py
- [ ] T061 [P] Add rate limiting to API endpoints in backend/api/routes/chat.py
- [ ] T062 [P] Create verification checklist for Phase 2 in specs/002-ai-chatbot-rag/
- [ ] T063 [P] Write comprehensive tests for backend services in backend/tests/
- [ ] T064 [P] Write component tests for chat widgets in docusaurus/physical-ai-book/src/components/ChatWidget/
- [ ] T065 [P] Update documentation in docusaurus/physical-ai-book/docs/
- [ ] T066 Run quickstart.md validation
- [ ] T067 Final integration testing of all components

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on US1 chat functionality
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May use US1/US2 components but should be independently testable

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
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence