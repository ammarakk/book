---
id: 3
title: auth-user-profiles-tasks
stage: tasks
date: 2025-12-27
surface: agent
model: Qwen
feature: auth-user-profiles
branch: 003-auth-user-profiles
user: User
command: /sp.tasks
labels: [tasks, authentication, user-profiles, betterauth]
links:
  spec: ../specs/003-auth-user-profiles/spec.md
  plan: ../specs/003-auth-user-profiles/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - ../specs/003-auth-user-profiles/tasks.md
tests:
  - specs/003-auth-user-profiles/tasks.md
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

Context for task generation: /sp.tasks Phase 3 — Authentication & User Profiles PHASE STATUS ------------ Phase: 3 State: OPEN Dependency: Phase 2 must be LOCKED Modification Rule: Tasks are executable only within Phase 3 scope -------------------------------------------------- TASK GROUP 1: AUTH ARCHITECTURE SETUP -------------------------------------------------- TASK 3.1 Title: Define Authentication Flow Description: Design the complete authentication flow using BetterAuth with JWT-based sessions. Acceptance Criteria: - Signup flow documented - Signin flow documented - JWT lifecycle defined (issue, refresh, expiry) - Logout flow defined - Session validation strategy clear Output: - Auth flow diagram (textual) - API contract summary TASK 3.2 Title: Setup BetterAuth Configuration Description: Configure BetterAuth for the project without implementing personalization or translation logic. Acceptance Criteria: - BetterAuth configured for email/password - JWT enabled - Environment-based configuration supported - No UI personalization hooks added Output: - BetterAuth config file - Auth environment variable list -------------------------------------------------- TASK GROUP 2: DATABASE & SCHEMA -------------------------------------------------- TASK 3.3 Title: Design User Schema (Neon) Description: Create database schema for users and their background profiles. Acceptance Criteria: - User table created - Fields include: - id - email - password_hash - created_at - Profile table created - Fields include: - user_id (FK) - software_background - hardware_background Output: - SQL schema definitions - ER-style relationship description TASK 3.4 Title: JWT Session Storage Strategy Description: Define how JWT sessions are validated and associated with users. Acceptance Criteria: - Stateless JWT validation defined - Token claims documented - Expiry and renewal strategy defined Output: - JWT payload schema - Validation logic outline -------------------------------------------------- TASK GROUP 3: BACKEND IMPLEMENTATION -------------------------------------------------- TASK 3.5 Title: Implement Signup API Description: Create signup endpoint that registers users and collects background data. Acceptance Criteria: - Accepts email & password - Accepts background questionnaire - Stores user and profile in Neon - Returns JWT on success - Handles validation errors Output: - /auth/signup endpoint implemented - Input/output schema documented TASK 3.6 Title: Implement Signin API Description: Create signin endpoint for existing users. Acceptance Criteria: - Email/password authentication - JWT issued on success - Error handling for invalid credentials Output: - /auth/signin endpoint implemented TASK 3.7 Title: Implement Auth Middleware Description: Protect authenticated routes using JWT validation. Acceptance Criteria: - Middleware validates token - Injects user context - Rejects unauthenticated requests Output: - Auth middleware module -------------------------------------------------- TASK GROUP 4: FRONTEND INTEGRATION -------------------------------------------------- TASK 3.8 Title: Create Signup UI Description: Build signup page integrated with BetterAuth. Acceptance Criteria: - Email & password fields - Software background question - Hardware background question - Form validation - Error handling UI Output: - Signup page component TASK 3.9 Title: Create Signin UI Description: Build signin page for existing users. Acceptance Criteria: - Email & password fields - JWT stored securely - Redirect on success Output: - Signin page component TASK 3.10 Title: Logged-In State Awareness Description: Update UI to detect authenticated users. Acceptance Criteria: - Auth state stored client-side - UI reacts to logged-in vs logged-out - No personalization or translation features exposed Output: - Auth context/provider - Header UI state changes -------------------------------------------------- TASK GROUP 5: SECURITY & VERIFICATION -------------------------------------------------- TASK 3.11 Title: Environment Variable Management Description: Define and validate required environment variables. Acceptance Criteria: - BETTERAUTH keys listed - JWT_SECRET defined - Neon connection string defined - Sample .env.example created Output: - .env.example file TASK 3.12 Title: Phase 3 Verification Checklist Description: Verify that Phase 3 meets all constitutional rules. Acceptance Criteria: - Signup works - Signin works - JWT sessions validated - No personalization logic present - No translation logic present - Phase 2 features untouched Output: - Phase 3 verification report -------------------------------------------------- PHASE 3 EXIT CONDITIONS -------------------------------------------------- Phase 3 can be LOCKED only if: - Users can sign up and sign in - User background data is stored - JWT authentication works end-to-end - UI reflects authenticated state - No Phase 4 or 5 features are present Any task outside this scope is constitutionally invalid.

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Response snapshot

I have successfully created a comprehensive tasks.md file for the Authentication & User Profiles feature. The tasks are organized according to the user stories from the specification with the following structure:

1. **Phase 1: Setup** - Project initialization and directory structure
2. **Phase 2: Foundational** - Core authentication infrastructure
3. **Phase 3: User Story 1** - Sign Up with Profile Information (Priority: P1)
4. **Phase 4: User Story 2** - Sign In and Maintain Authenticated State (Priority: P1)
5. **Phase 5: User Story 3** - Log Out and End Session (Priority: P2)
6. **Phase 6: User Story 4** - Access Protected Routes (Priority: P2)
7. **Phase 7: User Story 5** - Fetch and Display User Profile (Priority: P3)
8. **Phase 8: Polish & Cross-Cutting Concerns** - Security hardening and verification

Each task follows the required checklist format with:
- Checkbox: `- [ ]`
- Task ID: Sequential numbering (T001, T002, etc.)
- Parallel marker: [P] for tasks that can be executed in parallel
- Story label: [US1], [US2], etc. for user story-specific tasks
- Clear description with file paths

The tasks include dependencies between user stories, parallel execution opportunities, and independent test criteria for each user story. The MVP scope is defined as User Story 1 (Sign Up with Profile Information) which provides the core functionality.

## Outcome

- ✅ Impact: Created comprehensive task breakdown for authentication implementation
- 🧪 Tests: Tasks include test criteria for each user story
- 📁 Files: Created tasks.md with 61 specific, actionable tasks
- 🔁 Next prompts: Ready for implementation with /sp.implement
- 🧠 Reflection: Tasks follow proper format and enable incremental development

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All tasks follow required format
- Prompt variant (if applicable): Standard /sp.tasks workflow
- Next experiment (smallest change to try): Begin implementation with /sp.implement
