---
id: 3
title: auth-user-profiles-plan
stage: plan
date: 2025-12-27
surface: agent
model: Qwen
feature: auth-user-profiles
branch: 003-auth-user-profiles
user: User
command: /sp.plan
labels: [plan, authentication, user-profiles, betterauth]
links:
  spec: ../specs/003-auth-user-profiles/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - ../specs/003-auth-user-profiles/plan.md
  - ../specs/003-auth-user-profiles/research.md
  - ../specs/003-auth-user-profiles/data-model.md
  - ../specs/003-auth-user-profiles/quickstart.md
  - ../specs/003-auth-user-profiles/contracts/auth-api.md
tests:
  - specs/003-auth-user-profiles/plan.md
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType qwen`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---
/sp.plan /sp.plan Phase 3: Authentication & User Profiles

Objective:
Plan the implementation steps required to add secure authentication, user profiling, and session management using BetterAuth and Neon, strictly within Phase 3 scope as defined in the Constitution.

Phase Boundary:
- This plan ONLY covers authentication and user profiles
- No personalization logic
- No translation
- No chatbot changes
- No UI personalization buttons

--------------------------------------------------
DELIVERABLES
--------------------------------------------------

1. Authentication System
- Signup flow
- Signin flow
- Logout flow
- Session persistence
- JWT-based authentication

2. User Profile System
- User identity storage
- Background questionnaire storage
- Secure profile retrieval

3. Frontend Integration
- Auth pages (Signup / Signin)
- Logged-in state awareness
- Protected routes handling

--------------------------------------------------
TASK BREAKDOWN
--------------------------------------------------

Task 3.1: Environment Configuration
- Define required environment variables
- Secure handling of secrets
- Separate dev and prod readiness

Task 3.2: Database Schema Design
- Users table
- User profile table
- Auth session table (if required by BetterAuth)

Task 3.3: BetterAuth Integration
- Configure BetterAuth provider
- Connect BetterAuth to Neon PostgreSQL
- Setup JWT strategy
- Configure callback URLs

Task 3.4: Signup Flow
- Signup UI page
- Required fields:
  - Email
  - Password
- Background questionnaire:
  - Software experience level
  - Hardware/robotics experience level
- Persist user + profile data in Neon

Task 3.5: Signin Flow
- Signin UI page
- Credential validation
- JWT issuance
- Session storage (cookie or memory)

Task 3.6: Session Handling
- Logged-in state detection
- Token validation
- Session expiration handling
- Logout mechanism

Task 3.7: Frontend Auth State Awareness
- Detect authenticated user
- Display login/logout state in UI
- Restrict access where required
- No personalization logic

Task 3.8: API Security
- Protect profile endpoints
- Validate JWT on backend
- Prevent unauthorized access

--------------------------------------------------
DEPENDENCIES
--------------------------------------------------

- Phase 1: Completed and locked
- Phase 2: Completed and locked
- BetterAuth documentation
- Neon Serverless PostgreSQL
- FastAPI backend already available

--------------------------------------------------
NON-GOALS (EXPLICIT)
--------------------------------------------------

- No content personalization
- No translation features
- No chatbot logic changes
- No AI inference logic
- No UI redesign beyond auth pages

--------------------------------------------------
VERIFICATION CRITERIA
--------------------------------------------------

Phase 3 is complete when:
- Users can successfully sign up
- Users can sign in and receive a valid JWT
- User background data is stored in Neon
- Logged-in state is detectable in UI
- Protected endpoints reject unauthenticated requests
- Logout clears session correctly

--------------------------------------------------
LOCK CONDITIONS
--------------------------------------------------

Once verified:
- Authentication logic is frozen
- Database schema is frozen
- No refactoring allowed
- No additional auth features added

Phase 3 must be LOCKED before Phase 4 can be specified.

## Response snapshot

I have successfully created a comprehensive implementation plan for the Authentication & User Profiles feature. The plan includes:

1. **Technical Context**: Defined the technology stack (Python 3.11, JavaScript/TypeScript, BetterAuth, FastAPI, Neon PostgreSQL)
2. **Constitution Check**: Verified compliance with project principles and phase boundaries
3. **Project Structure**: Outlined the backend and frontend architecture
4. **Research**: Created research.md with decisions on authentication approach, database design, and session management
5. **Data Model**: Created data-model.md with User and User Profile entity definitions
6. **API Contracts**: Created auth-api.md with detailed API specifications
7. **Quickstart Guide**: Created quickstart.md with setup and testing instructions
8. **Agent Context Update**: Updated the Qwen agent context with new technology information

All required artifacts have been generated and the plan is ready for the next phase. The implementation follows the project constitution and stays within Phase 3 scope.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for authentication system
- 🧪 Tests: Plan includes testable API contracts and verification steps
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and auth-api.md
- 🔁 Next prompts: Ready for /sp.tasks to break plan into implementation tasks
- 🧠 Reflection: Plan follows best practices with clear architecture and scope boundaries

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All constitution checks passed
- Prompt variant (if applicable): Standard /sp.plan workflow
- Next experiment (smallest change to try): Move to task breakdown with /sp.tasks
