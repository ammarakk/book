---
id: 5
title: translation-system-tasks
stage: tasks
date: 2025-12-27
surface: agent
model: Qwen
feature: translation-system
branch: 005-translation-system
user: User
command: /sp.tasks
labels: [tasks, translation, english-urdu, claude-subagents]
links:
  spec: ../specs/005-translation-system/spec.md
  plan: ../specs/005-translation-system/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - ../specs/005-translation-system/tasks.md
tests:
  - specs/005-translation-system/tasks.md
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: /sp.tasks Phase 5 — Translation System (English ↔ Urdu) PHASE STATUS ------------ Phase: 5 State: OPEN Dependency: Phase 4 must be LOCKED Modification Rule: Tasks are executable only within Phase 5 scope -------------------------------------------------- TASK GROUP 1: TRANSLATION ARCHITECTURE SETUP -------------------------------------------------- TASK 5.1 Title: Define Translation Flow Description: Design the complete translation flow using Claude Code Subagents with deterministic, rule-based prompts. Acceptance Criteria: - Translation trigger documented (button at chapter start) - User authentication validation flow defined - Claude Code Subagent integration flow defined - Bidirectional translation flow defined (English ↔ Urdu) - Content preservation rules documented (technical terms, code blocks, formatting) Output: - Translation flow diagram (textual) - API contract summary TASK 5.2 Title: Setup Claude Code Subagent Framework Description: Configure Claude Code Subagents for translation without implementing multilingual support beyond English/Urdu. Acceptance Criteria: - Claude Code Subagent configured for translation - Deterministic, rule-based prompts implemented - Technical term preservation rules defined - Code block protection rules defined - No multilingual support beyond English/Urdu Output: - Claude Code Subagent config file - Translation prompt templates -------------------------------------------------- TASK GROUP 2: TRANSLATION DATA MODEL -------------------------------------------------- TASK 5.3 Title: Design Translation Session Schema Description: Create database schema for translation sessions and cached content. Acceptance Criteria: - TranslationSession table created - Fields include: - session_id - user_id (FK to Phase 3 users) - chapter_id - source_language (always "en") - target_language (always "ur") - translation_state - TranslatedContent table created - Fields include: - content_id - session_id (FK to TranslationSession) - original_content_id - original_text - translated_text - content_type - preservation_flags Output: - SQL schema definitions - ER-style relationship description TASK 5.4 Title: Translation State Management Strategy Description: Define how translation sessions are validated and associated with users. Acceptance Criteria: - Session-based translation validation defined - Token claims include user identification - Session expiry and cleanup strategy defined Output: - Session management schema - Validation logic outline -------------------------------------------------- TASK GROUP 3: BACKEND TRANSLATION IMPLEMENTATION -------------------------------------------------- TASK 5.5 Title: Implement Translation Request API Description: Create translation endpoint that accepts chapter content and user profile. Acceptance Criteria: - Accepts chapter_id and target language - Validates user authentication - Calls Claude Code Subagent with preservation rules - Returns translated content with metadata - Handles validation errors Output: - /api/translate/request endpoint implemented - Input/output schema documented TASK 5.6 Title: Implement Translation Retrieval API Description: Create endpoint for retrieving existing translation sessions. Acceptance Criteria: - Accepts session_id - Validates user owns session - Returns cached translation if available - Error handling for invalid sessions Output: - /api/translate/session/{session_id} endpoint implemented TASK 5.7 Title: Implement Translation Middleware Description: Protect translation endpoints using JWT validation. Acceptance Criteria: - Middleware validates token - Extracts user context - Rejects unauthenticated translation requests Output: - Translation auth middleware module -------------------------------------------------- TASK GROUP 4: FRONTEND TRANSLATION INTEGRATION -------------------------------------------------- TASK 5.8 Title: Create Translation Toggle Component Description: Build translation toggle button integrated with authentication state. Acceptance Criteria: - Button appears at start of each chapter - Button is hidden for non-authenticated users - Toggle behavior implemented (English ↔ Urdu) - Visual state indicates active translation - No multilingual features beyond English/Urdu Output: - TranslationToggle component TASK 5.9 Title: Create Translated Content Component Description: Build component to display translated content with preserved formatting. Acceptance Criteria: - Displays translated text with proper styling - Preserves code blocks in English - Maintains original formatting structure - Clear visual distinction from original content Output: - TranslatedContent component TASK 5.10 Title: Translation State Awareness Description: Update UI to detect and manage translation state. Acceptance Criteria: - Translation state stored client-side - UI reacts to translation active/inactive - Smooth transitions between languages - No multilingual features beyond English/Urdu Output: - Translation context/provider - UI state management -------------------------------------------------- TASK GROUP 5: AI TRANSLATION LOGIC -------------------------------------------------- TASK 5.11 Title: Claude Code Subagent Translation Logic Description: Implement Claude Code Subagent for English ↔ Urdu translation. Acceptance Criteria: - Preserves technical terminology (ROS 2, SLAM, URDF, etc.) - Preserves code blocks (no translation) - Preserves formatting and structure - Generates natural, professional Urdu - No hallucination or content expansion Output: - TranslationAgent implementation TASK 5.12 Title: Agent Skills for Content Preservation Description: Create Agent Skills for preserving technical content during translation. Acceptance Criteria: - TechnicalTermPreservation skill created - CodeBlockProtection skill created - FormattingMaintenance skill created - Skills are reusable across chapters - Technical terms remain unchanged Output: - Agent Skills library -------------------------------------------------- TASK GROUP 6: SECURITY & VERIFICATION -------------------------------------------------- TASK 5.13 Title: Environment Variable Management Description: Define and validate required environment variables for translation. Acceptance Criteria: - CLAUDE_API_KEY listed - JWT_SECRET defined - Database connection string defined - Sample .env.example created Output: - .env.example file TASK 5.14 Title: Phase 5 Verification Checklist Description: Verify that Phase 5 meets all constitutional rules. Acceptance Criteria: - Logged-in users can translate chapters - Technical accuracy is preserved - Code blocks remain unchanged - UI supports language toggling - No multilingual features beyond English/Urdu Output: - Phase 5 verification report -------------------------------------------------- PHASE 5 EXIT CONDITIONS -------------------------------------------------- Phase 5 can be LOCKED only if: - Logged-in users can translate chapters to Urdu - Technical accuracy is preserved - Code blocks remain unchanged - UI supports clean language toggling - No source content is altered - No additional languages are present Any task outside this scope is constitutionally invalid.

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Response snapshot

I have successfully created a comprehensive task breakdown for the Translation System (English ↔ Urdu) feature. The tasks are organized according to the user stories from the specification with the following structure:

1. **Phase 1: Setup** - Project initialization and basic structure (9 tasks)
2. **Phase 2: Foundational** - Core infrastructure that blocks all user stories (6 tasks)
3. **Phase 3: User Story 1** - Translate Chapter Content (Priority: P1) (10 tasks)
4. **Phase 4: User Story 2** - View Translated Content with Preserved Elements (Priority: P1) (5 tasks)
5. **Phase 5: User Story 3** - Access Translation Controls (Priority: P2) (4 tasks)
6. **Phase 6: Polish & Cross-Cutting Concerns** - Documentation, optimization, and validation (8 tasks)

Each task follows the required checklist format with:
- Checkbox: `- [ ]`
- Task ID: Sequential numbering (T001, T002, etc.)
- Parallel marker: [P] for tasks that can be executed in parallel
- Story label: [US1], [US2], [US3] for user story-specific tasks
- Clear description with file paths

The tasks include dependencies between phases, parallel execution opportunities, and independent test criteria for each user story. The MVP scope is defined as User Story 1 (Translate Chapter Content) which provides the core functionality.

## Outcome

- ✅ Impact: Created comprehensive task breakdown for translation system implementation
- 🧪 Tests: Tasks include testable acceptance criteria for each user story
- 📁 Files: Created tasks.md with 41 specific, actionable tasks
- 🔁 Next prompts: Ready for implementation with /sp.implement
- 🧠 Reflection: Tasks follow proper format and enable incremental development

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All tasks follow required format
- Prompt variant (if applicable): Standard /sp.tasks workflow
- Next experiment (smallest change to try): Begin implementation with /sp.implement