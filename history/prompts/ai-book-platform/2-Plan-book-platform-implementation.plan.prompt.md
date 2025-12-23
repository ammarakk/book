---
id: 2
title: Plan book platform implementation
stage: plan
date: 2025-12-24
surface: agent
model: gpt-4o
feature: ai-book-platform
branch: 001-ai-book-platform
user: User
command: /sp.plan
labels: [planning, architecture, design]
links:
  spec: specs/001-ai-book-platform/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-ai-book-platform/plan.md
 - specs/001-ai-book-platform/research.md
 - specs/001-ai-book-platform/data-model.md
 - specs/001-ai-book-platform/contracts/api-contracts.md
 - specs/001-ai-book-platform/quickstart.md
 - QWEN.md
tests:
 - none
---

## Prompt

---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
handoffs: 
  - label: Create Tasks
    agent: sp.tasks
    prompt: Break the plan into tasks
    send: true
  - label: Create Checklist
    agent: sp.checklist
    prompt: Create a checklist for the following domain...
---

## User Input

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

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.plan /sp.plan Physical AI & Humanoid Robotics Book Project

Project Name: Physical AI & Humanoid Robotics – AI/Spec-Driven Interactive Book

Goal:
Plan the step-by-step workflow to create, test, and deploy the interactive Physical AI & Humanoid Robotics book with integrated RAG chatbot, personalization, translation, and Neon-themed UI.

Phases & Steps:

Phase 1: Project Setup
- Step 1: Initialize project repository with Git.
- Step 2: Create Docusaurus project structure.
- Step 3: Set up Spec-Kit Plus folder structure:
  - spec/
  - spec/tasks/
  - spec/architecture/
  - spec/decisions/
- Step 4: Configure Claude Code Router with Qwen, Gemini, and Ollama providers.
- Step 5: Create .env file for API keys (Claude, Qwen, Gemini, Ollama).

Phase 2: Content Creation
- Step 1: Create `/sp.constitution` for project rules and vision.
- Step 2: Draft chapters for Modules 1-4.
- Step 3: Add hero section, images, and topic-related illustrations for each module.
- Step 4: Add body content with references and source links.
- Step 5: Include personalization and translation buttons at the start of each chapter.

Phase 3: Interactive Features
- Step 1: Embed RAG chatbot with Ollama LLM.
- Step 2: Add chatbot icon with animations in UI.
- Step 3: Implement personalized content feature for logged-in users.
- Step 4: Integrate translation feature (English ↔ Urdu).
- Step 5: Ensure chatbot can respond to user-selected text contextually.

Phase 4: User Authentication
- Step 1: Integrate BetterAuth with Neon for Sign-up and Sign-in.
- Step 2: Collect user software and hardware background during sign-up.
- Step 3: Test personalization of content based on user profile.

Phase 5: UI & Theme
- Step 1: Apply Neon Robotic theme to the book.
- Step 2: Implement animations for interactive buttons and chatbot.
- Step 3: Add hero section images and topic illustrations.
- Step 4: Create footer section with links and references.

Phase 6: Backend & RAG Integration
- Step 1: Set up Neon Serverless PostgreSQL for user and chatbot data.
- Step 2: Set up Qdrant Cloud Free Tier for embeddings.
- Step 3: Connect RAG chatbot to content embeddings for accurate retrieval.

Phase 7: Testing
- Step 1: Test book navigation, animations, and UI responsiveness.
- Step 2: Test RAG chatbot functionality with sample queries.
- Step 3: Test user sign-up, sign-in, personalization, and translation.
- Step 4: Test .env API key integration for all services.
- Step 5: Collect bug reports and fix errors.

Phase 8: Deployment
- Step 1: Prepare Docusaurus build for GitHub Pages.
- Step 2: Deploy book to GitHub Pages.
- Step 3: Verify chatbot, personalization, and translation work on live deployment.
- Step 4: Document final project structure and environment setup.

Phase 9: Documentation & References
- Step 1: Provide reference list for all sources used in chapters.
- Step 2: Document setup instructions for developers and students.
- Step 3: Include README with project overview, deployment, and testing instructions.

Success Criteria:
- Book content complete, up-to-date, and structured as per reference.
- RAG chatbot functional with Ollama LLM and responds accurately.
- User authentication with BetterAuth + Neon works correctly.
- Translation and personalization features work in all chapters.
- Neon-themed UI fully implemented with hero images, animations, and interactive elements.
- Deployment to GitHub Pages successful and fully functional.

## Response snapshot

The implementation planning workflow has been successfully executed with the following results:

**Branch**: `001-ai-book-platform`
**Implementation Plan Path**: `C:\Users\User\Documents\book\specs\001-ai-book-platform\plan.md`
**Generated Artifacts**:
- `specs/001-ai-book-platform/research.md` - Research summary resolving all NEEDS CLARIFICATION items
- `specs/001-ai-book-platform/data-model.md` - Complete data model with entities and relationships
- `specs/001-ai-book-platform/contracts/api-contracts.md` - API contracts for all required endpoints
- `specs/001-ai-book-platform/quickstart.md` - Quickstart guide for development setup
- Updated agent context in `QWEN.md` with project-specific information

The plan follows the constitution principles and creates a web application architecture with a Docusaurus frontend and Python backend services. All technology decisions have been researched and documented, with alternatives considered where appropriate.

## Outcome

- ✅ Impact: Comprehensive implementation plan created with all required design artifacts
- 🧪 Tests: No tests required for planning phase
- 📁 Files: Created multiple design documents including plan, research, data model, contracts, and quickstart
- 🔁 Next prompts: Ready to proceed with `/sp.tasks` to break the plan into implementation tasks
- 🧠 Reflection: The plan addresses all requirements from the feature specification while following constitutional principles

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A