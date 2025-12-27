# Implementation Plan: AI-Powered Content Personalization

**Branch**: `004-ai-personalization-engine` | **Date**: 2025-12-27 | **Spec**: [link to spec.md](./spec.md)
**Input**: Feature specification from `/specs/004-ai-personalization-engine/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan implements an AI-driven personalization system that adapts chapter-level explanations based on the logged-in user's background (software and hardware experience). The system uses Claude Code Subagents to generate personalized content that enhances understanding while preserving the original book content. The personalization is session-based and visually distinct from the canonical text.

## Technical Context

**Language/Version**: JavaScript/TypeScript for frontend components, Python 3.11 for backend services
**Primary Dependencies**: Claude Code Subagents, Agent Skills, Docusaurus, React, FastAPI, Neon Serverless PostgreSQL
**Storage**: Neon Serverless PostgreSQL for user profiles, static markdown files for book content
**Testing**: Jest for frontend components, pytest for backend services
**Target Platform**: Web application with Docusaurus frontend and FastAPI backend
**Project Type**: Web application (frontend + backend)
**Performance Goals**: <10 seconds for personalization generation, 98% success rate for Claude Code Subagents
**Constraints**: Original content must remain immutable, personalization is session-based only, JWT authentication required
**Scale/Scope**: Support up to 10,000 users with personalized content generation

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase Isolation Check
- [x] Only current phase features are being implemented
- [x] No future phase features are being implemented early
- [x] Previous phase is locked before starting current phase

### No Scope Creep Check
- [x] Features belong only to their assigned phase
- [x] No "small additions" from future phases
- [x] No refactors after phase lock

### AI-Friendly Structure Check
- [x] Clear specs exist before planning
- [x] Clear plans exist before implementation
- [x] Clear verification exists before locking

### Deterministic Execution Check
- [x] Every phase produces verifiable outputs
- [x] Ambiguity is resolved in Specify, not Implement

### Mandatory Phase Execution Lifecycle Check
- [x] Follows Specify → Plan → Implement → Verify → Lock sequence
- [x] No phase overlap allowed

### Locked Project Phases Check
- [x] Project phases completed in locked order
- [x] No skipping phases

## Project Structure

### Documentation (this feature)

```text
specs/004-ai-personalization-engine/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
docusaurus/
├── src/
│   ├── components/
│   │   ├── PersonalizeButton.js      # Personalization toggle button
│   │   ├── PersonalizedContent.js    # Component to display personalized content
│   │   └── AuthProvider.js           # Authentication context (from Phase 3)
│   ├── pages/
│   │   └── DocPage.js               # Modified DocPage to include personalization
│   ├── services/
│   │   └── personalization.js       # Service to interact with Claude Code Subagents
│   └── utils/
│       └── auth.js                  # Authentication utilities (from Phase 3)
└── static/
    └── docs/                        # Original book content (from Phase 1)

backend/
├── src/
│   ├── services/
│   │   └── personalization.py       # Backend service for personalization
│   ├── api/
│   │   └── personalization.py       # API endpoints for personalization
│   └── models/
│       └── personalization.py       # Data models for personalization
└── tests/
    └── unit/
        └── test_personalization.py  # Unit tests for personalization service

agents/
├── claude-subagents/
│   ├── beginner-agent.py            # Agent for beginner-level personalization
│   ├── intermediate-agent.py        # Agent for intermediate-level personalization
│   ├── advanced-agent.py            # Agent for advanced-level personalization
│   └── agent-skills/
│       ├── simplification.py        # Skill for content simplification
│       ├── elaboration.py           # Skill for technical elaboration
│       └── terminology-check.py     # Skill for terminology validation
```

**Structure Decision**: Web application structure with frontend (Docusaurus) components for UI and interaction, backend (FastAPI) services for personalization logic, and agent directory for Claude Code Subagents and Agent Skills, following the architecture established in previous phases.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
