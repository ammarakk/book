<!-- SYNC IMPACT REPORT
Version change: N/A → 1.0.0
Modified principles: N/A (new constitution)
Added sections: All principles and sections
Removed sections: N/A
Templates requiring updates: 
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated  
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ updated
Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics – AI/Spec-Driven Interactive Book Constitution

## Core Principles

### Phase Isolation
Work is executed strictly phase-by-phase. Only one phase is 'open' at a time. No future phase features may be implemented early. Once a phase is locked, it must not be modified.

### No Scope Creep
Features belong only to their assigned phase. 'Small additions' from future phases are forbidden. Refactors after phase lock are not allowed.

### AI-Friendly Structure
Clear specs before planning. Clear plans before implementation. Clear verification before locking.

### Deterministic Execution
Every phase must produce verifiable outputs. Ambiguity is resolved in Specify, not Implement.

### Mandatory Phase Execution Lifecycle
Each phase MUST follow this exact sequence: Specify → Plan → Implement → Verify → Lock. No phase overlap is allowed.

### Locked Project Phases
Project phases must be completed in locked order: Phase 1 (Book Foundation), Phase 2 (AI Chatbot), Phase 3 (Authentication), Phase 4 (Personalization), Phase 5 (Translation).

## Content Scope
Topic: Physical AI & Humanoid Robotics. Modules: 1. The Robotic Nervous System (ROS 2), 2. The Digital Twin (Gazebo & Unity), 3. The AI-Robot Brain (NVIDIA Isaac™), 4. Vision-Language-Action (VLA), 5. Capstone: Autonomous Humanoid. Includes: Weekly breakdown, Learning outcomes, Hardware requirements, On-prem vs cloud lab architectures, Real-world robot references.

## Tech Stack
Frontend: Docusaurus, Custom React components, Neon robotic theme, Animations (CSS / Framer Motion). Backend: FastAPI, Neon Serverless PostgreSQL, Qdrant Cloud (Free Tier). AI: Claude Code (orchestrator), Ollama (LLM for chatbot), Claude Code Subagents, Agent Skills. Auth: BetterAuth, JWT-based sessions.

## Governance
Constitution is immutable. Each phase requires: Specify → Plan → Implement → Verify → Lock. No phase overlap. No silent changes. No 'quick fixes' after lock. All AI behavior must follow spec boundaries.

**Version**: 1.0.0 | **Ratified**: 2025-01-04 | **Last Amended**: 2025-01-04