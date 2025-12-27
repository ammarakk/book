---
id: 4
title: ai-personalization-engine-tasks
stage: tasks
date: 2025-12-27
surface: agent
model: Qwen
feature: ai-personalization-engine
branch: 004-ai-personalization-engine
user: User
command: /sp.tasks
labels: [tasks, personalization, ai, claude-subagents]
links:
  spec: ../specs/004-ai-personalization-engine/spec.md
  plan: ../specs/004-ai-personalization-engine/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - ../specs/004-ai-personalization-engine/tasks.md
tests:
  - specs/004-ai-personalization-engine/tasks.md
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

Context for task generation: /sp.tasks Phase 4 — Personalization Engine PHASE STATUS ------------ Phase: 4 State: OPEN Dependency: Phase 3 must be LOCKED Modification Rule: Tasks are executable only within Phase 4 scope -------------------------------------------------- TASK GROUP 1: UI LAYER -------------------------------------------------- TASK 4.1 Title: Add Personalize Content Button Description: Add "Personalize Content" button to chapter template with proper visibility logic. Acceptance Criteria: - Button appears at start of each chapter - Button is hidden for non-authenticated users - Toggle behavior implemented (on/off) - Button has clear CTA styling Output: - PersonalizeButton component implemented TASK 4.2 Title: Implement Visual Distinction Description: Ensure personalized content is visually distinct from original content. Acceptance Criteria: - Clear visual separation between original and personalized content - Smooth animations on reveal - CSS/Framer Motion animations implemented Output: - PersonalizedContent component with visual styling -------------------------------------------------- TASK GROUP 2: USER CONTEXT RESOLUTION -------------------------------------------------- TASK 4.3 Title: Fetch User Profile Description: Retrieve user profile from Neon DB and normalize background data. Acceptance Criteria: - User profile fetched from Neon DB - Background data normalized into categories (Beginner/Intermediate/Advanced) - Context passed to AI layer Output: - User context resolution service -------------------------------------------------- TASK GROUP 3: AI PERSONALIZATION LAYER -------------------------------------------------- TASK 4.4 Title: Define Claude Code Subagents Description: Create specialized agents for different user backgrounds. Acceptance Criteria: - BeginnerAgent implemented - IntermediateAgent implemented - AdvancedAgent implemented - Agents follow constitution rules Output: - Claude Code Subagent implementations TASK 4.5 Title: Create Agent Skills Description: Develop reusable skills for the Claude Code Subagents. Acceptance Criteria: - Simplification skill created - Technical elaboration skill created - Skills are reusable across chapters - Technical terms remain unchanged Output: - Agent Skills library -------------------------------------------------- TASK GROUP 4: CONTENT INJECTION -------------------------------------------------- TASK 4.6 Title: Implement Content Injection Description: Render personalized content with proper isolation and preservation. Acceptance Criteria: - Personalized content rendered in isolated UI container - Original content preserved (markdown, code blocks, diagrams) - Visual separation maintained Output: - Content injection mechanism -------------------------------------------------- TASK GROUP 5: SAFETY & VALIDATION -------------------------------------------------- TASK 4.7 Title: Implement Safety Measures Description: Add validation and safety measures to personalization flow. Acceptance Criteria: - Token and length limits enforced - Terminology validated against chapter glossary - Cross-chapter contamination prevented Output: - Safety and validation mechanisms -------------------------------------------------- PHASE 4 EXIT CONDITIONS -------------------------------------------------- Phase 4 can be LOCKED only if: - All acceptance criteria in /sp.specify are met - No Phase 5 features are present - Personalization works consistently across chapters Any task outside this scope is constitutionally invalid.

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Response snapshot

I have successfully created a comprehensive tasks.md file for the AI-Powered Content Personalization feature. The tasks are organized according to the user stories from the specification with the following structure:

1. **Phase 1: Setup** - Project initialization and directory structure
2. **Phase 2: Foundational** - Core infrastructure that blocks all user stories
3. **Phase 3: User Story 1** - Personalize Chapter Content (Priority: P1)
4. **Phase 4: User Story 2** - View Personalized Content with Visual Distinction (Priority: P1)
5. **Phase 5: User Story 3** - Access Personalization Controls (Priority: P2)
6. **Phase 6: Agent Skills Implementation** - Reusable agent skills for Claude Code Subagents
7. **Phase 7: Polish & Cross-Cutting Concerns** - Security, performance, and validation

Each task follows the required checklist format with:
- Checkbox: `- [ ]`
- Task ID: Sequential numbering (T001, T002, etc.)
- Parallel marker: [P] for tasks that can be executed in parallel
- Story label: [US1], [US2], etc. for user story-specific tasks
- Clear description with file paths

The tasks include dependencies between phases, parallel execution opportunities, and independent test criteria for each user story. The MVP scope is defined as User Story 1 (Personalize Chapter Content) which provides the core functionality.

## Outcome

- ✅ Impact: Created comprehensive task breakdown for personalization implementation
- 🧪 Tests: Tasks include test criteria for each user story
- 📁 Files: Created tasks.md with 46 specific, actionable tasks
- 🔁 Next prompts: Ready for implementation with /sp.implement
- 🧠 Reflection: Tasks follow proper format and enable incremental development

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All tasks follow required format
- Prompt variant (if applicable): Standard /sp.tasks workflow
- Next experiment (smallest change to try): Begin implementation with /sp.implement
