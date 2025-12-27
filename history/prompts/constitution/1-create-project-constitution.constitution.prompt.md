---
id: 1
title: create-project-constitution
stage: constitution
date: 2025-01-04
surface: agent
model: gpt-4
feature: none
branch: main
user: User
command: /sp.constitution
labels: ["constitution", "setup", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\\Users\\User\\Documents\\books\\.specify\\memory\\constitution.md
 - C:\\Users\\User\\Documents\\books\\.specify\\templates\\plan-template.md
 - C:\\Users\\User\\Documents\\books\\.specify\\templates\\spec-template.md
 - C:\\Users\\User\\Documents\\books\\.specify\\templates\\tasks-template.md
 - C:\\Users\\User\\Documents\\books\\.claude\\commands\\sp.constitution.md
tests:
 - none
---

## Prompt

```
/sp.constitution /sp.constitution Physical AI & Humanoid Robotics Book Project

Project Name:
Physical AI & Humanoid Robotics – AI/Spec-Driven Interactive Book

Vision:
Build a world-class, AI-native, interactive textbook that bridges the gap between digital intelligence and physical embodiment. The book will teach students how to design, simulate, and deploy humanoid robots using modern robotics middleware, physics simulation, embodied AI, and vision-language-action systems, while integrating AI-driven personalization, translation, and conversational assistance.

This project is designed to be:
- AI-first
- Spec-driven
- Phase-locked
- Production-ready
- Hackathon-scorable

Single Source of Truth:
This constitution is the highest authority document. All future specifications, plans, and implementations must strictly follow the rules, phases, and boundaries defined here.

--------------------------------------------------
CORE PRINCIPLES
--------------------------------------------------

1. Phase Isolation
- Work is executed strictly phase-by-phase
- Only one phase is “open” at a time
- No future phase features may be implemented early
- Once a phase is locked, it must not be modified

2. No Scope Creep
- Features belong only to their assigned phase
- “Small additions” from future phases are forbidden
- Refactors after phase lock are not allowed

3. AI-Friendly Structure
- Clear specs before planning
- Clear plans before implementation
- Clear verification before locking

4. Deterministic Execution
- Every phase must produce verifiable outputs
- Ambiguity is resolved in Specify, not Implement

--------------------------------------------------
MANDATORY PHASE EXECUTION LIFECYCLE
--------------------------------------------------

Each phase MUST follow this exact sequence:

1. Specify
- Scope is explicitly defined
- Only the current phase is open
- All other phases are locked

2. Plan
- Tasks are broken down
- Dependencies are identified
- No new scope is introduced

3. Implement
- Code and content are written strictly per plan
- No speculative or future work

4. Verify
- Outputs are checked against the specification
- Acceptance criteria must be met

5. Lock
- Phase is frozen permanently
- No refactors
- No feature additions
- No reopening of scope

⚠️ Any attempt to partially implement a future phase
(e.g., “Phase 1 is almost done, let’s add a small Phase 2 feature”)
is strictly forbidden and must be rejected.

--------------------------------------------------
PROJECT PHASES (LOCKED ORDER)
--------------------------------------------------

Phase 1: Book Foundation (Content & Structure)
Goal:
Create the complete Physical AI & Humanoid Robotics book using Docusaurus.

Scope:
- Docusaurus project setup
- Book structure, modules, chapters
- Hero section with topic-related images
- Body content with references and sources
- Footer with links and citations
- Neon robotic visual theme (static)
- GitHub Pages readiness (no deployment yet)

Out of Scope:
- Chatbot
- Authentication
- Translation
- Personalization
- Backend services

--------------------------------------------------

Phase 2: AI Chatbot (RAG System)
Goal:
Embed an AI chatbot capable of answering questions from book content.

Scope:
- Chat UI embedded in book
- Chatbot icon with animation
- LLM: Ollama
- Retrieval-Augmented Generation (RAG)
- Context-aware answers
- Selected-text-only answering
- Qdrant Cloud (vector store)
- Neon Serverless Postgres (metadata)
- FastAPI backend

Out of Scope:
- User login
- Personalization
- Translation

--------------------------------------------------

Phase 3: Authentication & User Profiles
Goal:
Enable secure user identity and learning context.

Scope:
- Signup & Signin using BetterAuth
- Neon database integration
- Signup questionnaire:
  - Software background
  - Hardware background
- Session handling (JWT based)
- Logged-in state awareness in UI

Out of Scope:
- Content personalization logic
- Translation

--------------------------------------------------

Phase 4: Personalization Engine
Goal:
Adapt content based on user background.

Scope:
- “Personalize Content” button per chapter
- AI-generated explanations based on user profile
- Claude Code Subagents for reusable intelligence
- No content rewriting at source level
- Personalization only for logged-in users

--------------------------------------------------

Phase 5: Translation System
Goal:
Enable bilingual learning.

Scope:
- “Translate to Urdu” button per chapter
- English ↔ Urdu translation
- Logged-in users only
- Translation must preserve:
  - Technical terms
  - Code references
  - Structure

--------------------------------------------------
CONTENT SCOPE (LOCKED)
--------------------------------------------------

Topic:
Physical AI & Humanoid Robotics

Modules:
1. The Robotic Nervous System (ROS 2)
2. The Digital Twin (Gazebo & Unity)
3. The AI-Robot Brain (NVIDIA Isaac™)
4. Vision-Language-Action (VLA)
5. Capstone: Autonomous Humanoid

Includes:
- Weekly breakdown
- Learning outcomes
- Hardware requirements
- On-prem vs cloud lab architectures
- Real-world robot references

--------------------------------------------------
TECH STACK (LOCKED)
--------------------------------------------------

Frontend:
- Docusaurus
- Custom React components
- Neon robotic theme
- Animations (CSS / Framer Motion)

Backend:
- FastAPI
- Neon Serverless PostgreSQL
- Qdrant Cloud (Free Tier)

AI:
- Claude Code (orchestrator)
- Ollama (LLM for chatbot)
- Claude Code Subagents
- Agent Skills

Auth:
- BetterAuth
- JWT-based sessions

--------------------------------------------------
GOVERNANCE RULES
--------------------------------------------------

- Constitution is immutable
- Each phase requires:
  Specify → Plan → Implement → Verify → Lock
- No phase overlap
- No silent changes
- No “quick fixes” after lock
- All AI behavior must follow spec boundaries

--------------------------------------------------
SUCCESS DEFINITION
--------------------------------------------------

The project is successful when:
- The book is fully published on GitHub Pages
- Chatbot answers accurately from book content
- Users can sign up, sign in, and be profiled
- Content can be personalized per user
- Content can be translated to Urdu
- UI is interactive, animated, and stable
- All phases are completed without scope violations

--------------------------------------------------
FINAL NOTE
--------------------------------------------------

This constitution defines WHAT is allowed.
Future Specify documents define HOW it is done.
Implementation defines EXECUTION only.

Any request that violates this constitution must be rejected.
```

## Response snapshot

I have successfully created the project constitution for the Physical AI & Humanoid Robotics Book Project. Here's what was accomplished:

1. Created the main constitution file at `.specify/memory/constitution.md` with all the specified principles and project details.

2. Updated dependent templates to include constitution compliance checks:
   - `.specify/templates/plan-template.md`
   - `.specify/templates/spec-template.md`
   - `.specify/templates/tasks-template.md`

3. Updated the constitution command file to remove agent-specific references.

The constitution includes all the required principles:
- Phase Isolation
- No Scope Creep
- AI-Friendly Structure
- Deterministic Execution
- Mandatory Phase Execution Lifecycle
- Locked Project Phases

It also contains the required sections for Content Scope, Tech Stack, and Governance, all aligned with the Physical AI & Humanoid Robotics Book Project requirements.

The version is set to 1.0.0 as this is the initial creation of the constitution.

## Outcome

- ✅ Impact: Created comprehensive project constitution with all required principles and governance structure
- 🧪 Tests: No tests required for this documentation task
- 📁 Files: 5 files updated to ensure consistency across project templates
- 🔁 Next prompts: Ready for project specification phase based on this constitution
- 🧠 Reflection: The constitution provides a solid foundation for the project with clear phase-based execution lifecycle

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for this documentation task
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin with project specification based on this constitution