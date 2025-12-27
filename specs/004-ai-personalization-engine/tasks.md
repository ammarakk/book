# Tasks: AI-Powered Content Personalization

**Input**: Design documents from `/specs/004-ai-personalization-engine/`
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

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan
- [X] T002 [P] Create docusaurus/src/components directory
- [X] T003 [P] Create docusaurus/src/services directory
- [X] T004 [P] Create backend/src/services directory
- [X] T005 [P] Create backend/src/api directory
- [X] T006 [P] Create backend/src/models directory
- [X] T007 [P] Create agents/claude-subagents directory
- [X] T008 [P] Create agents/claude-subagents/agent-skills directory

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T009 [P] Implement personalization session model in backend/src/models/personalization.py
- [X] T010 [P] Implement personalized content model in backend/src/models/personalization.py
- [X] T011 [P] Setup API routing and middleware structure in backend/src/api/personalization.py
- [X] T012 [P] Create Claude Code Subagent base framework in agents/claude-subagents/base_agent.py
- [X] T013 [P] Create Agent Skills base framework in agents/claude-subagents/agent-skills/base_skill.py
- [X] T014 [P] Setup environment configuration management for Claude API in backend/src/config/personalization.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Personalize Chapter Content (Priority: P1) 🎯 MVP

**Goal**: Enable authenticated users to personalize chapter content based on their software and hardware experience level

**Independent Test**: Can be fully tested by logging in with a user profile, navigating to a chapter, clicking the "Personalize Content" button, and verifying that additional explanations and examples appear that are relevant to the user's background.

### Implementation for User Story 1

- [X] T015 [P] [US1] Create PersonalizeButton component in docusaurus/src/components/PersonalizeButton.js
- [X] T016 [P] [US1] Create PersonalizedContent component in docusaurus/src/components/PersonalizedContent.js
- [X] T017 [US1] Implement personalization service in docusaurus/src/services/personalization.js
- [ ] T018 [US1] Implement personalization API endpoint in backend/src/api/personalization.py
- [X] T019 [US1] Implement personalization service in backend/src/services/personalization.py
- [X] T020 [US1] Create BeginnerAgent in agents/claude-subagents/beginner-agent.py
- [X] T021 [US1] Create IntermediateAgent in agents/claude-subagents/intermediate-agent.py
- [X] T022 [US1] Create AdvancedAgent in agents/claude-subagents/advanced-agent.py
- [ ] T023 [US1] Integrate personalization into DocPage in docusaurus/src/pages/DocPage.js
- [X] T024 [US1] Add visual distinction styling for personalized content in docusaurus/src/css/personalization.css

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Personalized Content with Visual Distinction (Priority: P1)

**Goal**: Allow authenticated users to clearly distinguish between original book content and personalized content

**Independent Test**: Can be fully tested by activating personalization and verifying that original and personalized content have clear visual distinctions.

### Implementation for User Story 2

- [X] T025 [P] [US2] Enhance PersonalizedContent component with expandable sections in docusaurus/src/components/PersonalizedContent.js
- [X] T026 [US2] Implement smooth animation for content reveal in docusaurus/src/components/PersonalizedContent.js
- [X] T027 [US2] Add CSS animations using Framer Motion in docusaurus/src/components/PersonalizedContent.js
- [X] T028 [US2] Update personalization API to include metadata for visual distinction in backend/src/api/personalization.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Access Personalization Controls (Priority: P2)

**Goal**: Ensure the "Personalize Content" button is only visible when the user is logged in

**Independent Test**: Can be fully tested by checking the visibility of the personalization button when logged in versus when logged out.

### Implementation for User Story 3

- [X] T029 [P] [US3] Update PersonalizeButton to check authentication state in docusaurus/src/components/PersonalizeButton.js
- [X] T030 [US3] Implement button disable functionality when personalization is active in docusaurus/src/components/PersonalizeButton.js
- [X] T031 [US3] Add JWT authentication validation to personalization endpoint in backend/src/api/personalization.py
- [X] T032 [US3] Update personalization service to verify user authentication in backend/src/services/personalization.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Agent Skills Implementation

**Goal**: Create reusable agent skills for the Claude Code Subagents

### Implementation

- [X] T033 [P] Create ContentSimplification skill in agents/claude-subagents/agent-skills/simplification.py
- [X] T034 [P] Create TechnicalElaboration skill in agents/claude-subagents/agent-skills/elaboration.py
- [X] T035 [P] Create TerminologyValidation skill in agents/claude-subagents/agent-skills/terminology-check.py
- [X] T036 Integrate agent skills with Claude Code Subagents in agents/claude-subagents/beginner-agent.py
- [X] T037 Integrate agent skills with Claude Code Subagents in agents/claude-subagents/intermediate-agent.py
- [X] T038 Integrate agent skills with Claude Code Subagents in agents/claude-subagents/advanced-agent.py

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T039 [P] Documentation updates in docs/personalization.md
- [X] T040 Code cleanup and refactoring
- [ ] T041 Performance optimization for personalization generation
- [ ] T042 Security hardening for API endpoints
- [X] T043 Run quickstart.md validation
- [X] T044 Add error handling for Claude Code Subagent unavailability
- [ ] T045 Add rate limiting to personalization endpoints
- [ ] T046 Add caching for personalized content to improve performance

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Agent Skills (Phase 6)**: Depends on foundational completion
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