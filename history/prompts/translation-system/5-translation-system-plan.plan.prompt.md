---
id: 5
title: translation-system-plan
stage: plan
date: 2025-12-27
surface: agent
model: Qwen
feature: translation-system
branch: 005-translation-system
user: User
command: /sp.plan
labels: [plan, translation, english-urdu, claude-subagents]
links:
  spec: ../specs/005-translation-system/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - ../specs/005-translation-system/plan.md
  - ../specs/005-translation-system/research.md
  - ../specs/005-translation-system/data-model.md
  - ../specs/005-translation-system/quickstart.md
  - ../specs/005-translation-system/contracts/translation-api.md
tests:
  - specs/005-translation-system/plan.md
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

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
/sp.plan /sp.plan Phase 5 — Translation System (English ↔ Urdu)

Phase Objective:
Implement a controlled, high-quality English ↔ Urdu translation system for book chapters, accessible via UI buttons, preserving technical accuracy and structure.

--------------------------------------------------
PLANNING CONSTRAINTS
--------------------------------------------------

- Phase 5 ONLY
- All previous phases are LOCKED
- No changes to:
  - Book source content
  - Chatbot logic
  - Authentication flow
  - Personalization engine
- Translation is an overlay, not a rewrite
- Logged-in users ONLY

--------------------------------------------------
SYSTEM ARCHITECTURE PLAN
--------------------------------------------------

Frontend:
- Docusaurus custom React components
- Per-chapter UI control:
  - "Translate to Urdu"
  - "View Original (English)"
- Visual state indicator (Translated / Original)
- Smooth UI animation on language switch

Backend:
- FastAPI translation endpoint
- Stateless request-based translation
- JWT verification (reuse Phase 3 auth)

AI Layer:
- Translation engine:
  - LLM via Ollama OR Claude Code Subagent
- Prompt rules:
  - Preserve technical terms
  - Preserve headings, lists, code blocks
  - Preserve formatting and structure
  - No hallucination
  - No simplification unless explicitly allowed

--------------------------------------------------
DATA FLOW PLAN
--------------------------------------------------

1. User clicks "Translate to Urdu"
2. Frontend checks:
   - User authenticated
3. Chapter content sent to backend
4. Backend:
   - Verifies JWT
   - Applies translation prompt rules
5. AI returns structured Urdu translation
6. Frontend renders translated content
7. User can toggle back to English instantly

--------------------------------------------------
CONTENT SAFETY RULES
--------------------------------------------------

- Code blocks MUST NOT be translated
- File paths, commands, API names unchanged
- English technical terms may include:
  - Urdu explanation in brackets (optional)
- Headings hierarchy preserved (H1 → H6)
- Lists and tables preserved exactly

--------------------------------------------------
QUALITY CONTROL PLAN
--------------------------------------------------

Verification checklist per chapter:
- No missing sections
- No reordered paragraphs
- No altered code
- Correct Urdu grammar
- Technical meaning preserved

--------------------------------------------------
NON-GOALS (EXPLICITLY EXCLUDED)
--------------------------------------------------

- Auto-translation on page load
- Guest user translation
- Saving translated content to database
- Multi-language support beyond Urdu
- Audio / voice translation

--------------------------------------------------
PHASE COMPLETION CRITERIA
--------------------------------------------------

Phase 5 is considered complete when:
- Every chapter has a working Translate button
- Translation works only for logged-in users
- Urdu output preserves technical accuracy
- Users can toggle languages without reload
- No impact on previous phases

--------------------------------------------------
PHASE LOCK RULE
--------------------------------------------------

Once Phase 5 is verified:
- Translation logic is frozen
- Prompt rules are immutable
- No additional languages allowed

End of /sp.plan Phase 5

## Response snapshot

I have successfully created a comprehensive implementation plan for the Translation System (English ↔ Urdu) feature. The plan includes:

1. **Technical Context**: Defined the technology stack (JavaScript/TypeScript for frontend, Python 3.11 for backend, Claude Code Subagents for AI translation)

2. **Constitution Compliance Check**: Verified that all project phases are properly locked and the feature belongs to the current phase

3. **Project Structure**: Outlined the directory structure for both frontend and backend components

4. **Research**: Created research.md with decisions on:
   - Claude Code Subagent architecture for translation
   - Frontend component architecture
   - Session-based caching approach
   - Technical term preservation strategy
   - Code block protection mechanism

5. **Data Model**: Created data-model.md with entities for:
   - Translation Session
   - Translated Content

6. **API Contracts**: Created translation-api.md with specifications for:
   - Translation request endpoint
   - Session retrieval endpoint
   - Claude Code Subagent integration
   - Agent Skills definitions

7. **Quickstart Guide**: Created quickstart.md with setup and testing instructions

8. **Agent Context Update**: Updated the Qwen agent context with new technology information from this plan

The plan follows the project constitution and phase requirements, ensuring that the translation system preserves technical accuracy while providing multilingual access for authenticated users. All implementation artifacts have been created and the plan is ready for the next phase.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for translation system
- 🧪 Tests: Plan includes testable API contracts and verification steps
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and translation-api.md
- 🔁 Next prompts: Ready for /sp.tasks to break plan into implementation tasks
- 🧠 Reflection: Plan follows best practices with clear architecture and scope boundaries

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All constitution checks passed
- Prompt variant (if applicable): Standard /sp.plan workflow
- Next experiment (smallest change to try): Move to task breakdown with /sp.tasks