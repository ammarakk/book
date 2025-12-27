---
id: 4
title: ai-personalization-engine-plan
stage: plan
date: 2025-12-27
surface: agent
model: Qwen
feature: ai-personalization-engine
branch: 004-ai-personalization-engine
user: User
command: /sp.plan
labels: [plan, personalization, ai, claude-subagents]
links:
  spec: ../specs/004-ai-personalization-engine/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - ../specs/004-ai-personalization-engine/plan.md
  - ../specs/004-ai-personalization-engine/research.md
  - ../specs/004-ai-personalization-engine/data-model.md
  - ../specs/004-ai-personalization-engine/quickstart.md
  - ../specs/004-ai-personalization-engine/contracts/personalization-api.md
tests:
  - specs/004-ai-personalization-engine/plan.md
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
/sp.plan /sp.plan

Project: Physical AI & Humanoid Robotics – AI/Spec-Driven Interactive Book
Phase: 4
Phase Name: Personalization Engine

--------------------------------------------------
EXECUTION STRATEGY
--------------------------------------------------

Implement personalization as a non-destructive, runtime augmentation layer that sits above static book content.

--------------------------------------------------
TASK BREAKDOWN
--------------------------------------------------

1. UI Layer
- Add "Personalize Content" button to chapter template
- Hide button for non-authenticated users
- Implement toggle behavior (on/off)

2. User Context Resolution
- Fetch user profile from Neon DB
- Normalize background data into categories:
  - Beginner / Intermediate / Advanced
- Pass resolved context to AI layer

3. AI Personalization Layer
- Define Claude Code Subagents:
  - BeginnerAgent
  - IntermediateAgent
  - AdvancedAgent
- Create Agent Skills for:
  - Simplification
  - Deep technical elaboration
- Standardize prompt structure

4. Content Injection
- Render personalized content in isolated UI container
- Ensure visual separation from canonical text
- Preserve markdown, code blocks, and diagrams

5. Safety & Validation
- Enforce token and length limits
- Validate terminology against chapter glossary
- Prevent cross-chapter contamination

--------------------------------------------------
DEPENDENCIES
--------------------------------------------------

- Phase 1: Book content and structure (LOCKED)
- Phase 2: Chatbot system (LOCKED)
- Phase 3: Authentication and user profiles (LOCKED)

--------------------------------------------------
TESTING & VERIFICATION
--------------------------------------------------

- Test personalization for:
  - Beginner-only users
  - Mixed background users
- Verify toggle behavior
- Confirm zero changes to source markdown
- Confirm personalization disappears when logged out

--------------------------------------------------
DELIVERABLES
--------------------------------------------------

- Personalized chapter UI
- Claude Code Subagents
- Agent Skills library
- Verified non-destructive personalization flow

--------------------------------------------------
EXIT CONDITIONS
--------------------------------------------------

Phase 4 may be locked only when:
- All acceptance criteria in /sp.specify are met
- No Phase 5 features exist
- Personalization works consistently across chapters

--------------------------------------------------
LOCK READINESS
--------------------------------------------------

After verification:
- Freeze personalization logic
- Proceed to "Specify Phase 5"

This plan defines HOW Phase 4 will be executed.

## Response snapshot

I have successfully created a comprehensive implementation plan for the AI-Powered Content Personalization feature. The plan includes:

1. **Technical Context**: Defined the technology stack (JavaScript/TypeScript, Python 3.11, Claude Code Subagents, Docusaurus, FastAPI, Neon PostgreSQL)
2. **Constitution Check**: Verified compliance with project principles and phase boundaries
3. **Project Structure**: Outlined the frontend, backend, and agent architecture
4. **Research**: Created research.md with decisions on Claude Code Subagent architecture, frontend components, session-based personalization, visual distinction approach, and user profile integration
5. **Data Model**: Created data-model.md with Personalization Session and Personalized Content entities
6. **API Contracts**: Created personalization-api.md with endpoints for requesting and retrieving personalized content
7. **Quickstart Guide**: Created quickstart.md with setup and testing instructions
8. **Agent Context Update**: Updated the Qwen agent context with new technology information from this plan

All required artifacts have been generated and the plan is ready for the next phase. The implementation follows the project constitution and stays within Phase 4 scope.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for personalization engine
- 🧪 Tests: Plan includes testable API contracts and verification steps
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and personalization-api.md
- 🔁 Next prompts: Ready for /sp.tasks to break plan into implementation tasks
- 🧠 Reflection: Plan follows best practices with clear architecture and scope boundaries

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All constitution checks passed
- Prompt variant (if applicable): Standard /sp.plan workflow
- Next experiment (smallest change to try): Move to task breakdown with /sp.tasks
