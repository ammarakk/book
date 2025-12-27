# Implementation Plan: Translation System (English ↔ Urdu)

**Branch**: `005-translation-system` | **Date**: 2025-12-27 | **Spec**: [link to spec.md](./spec.md)
**Input**: Feature specification from `/specs/005-translation-system/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan implements a bilingual translation system that allows authenticated users to toggle between English and Urdu versions of book content. The system uses Claude Code Subagents to generate accurate translations while preserving technical terminology, code blocks, and formatting. The translation is session-based and overlays the original content without modifying the source material.

## Technical Context

**Language/Version**: JavaScript/TypeScript (frontend), Python 3.11 (backend)
**Primary Dependencies**: Docusaurus (frontend framework), FastAPI (backend framework), Claude Code Subagents (AI translation), react-i18next (internationalization), js-cookie (session management)
**Storage**: Neon Serverless PostgreSQL (user authentication data), static markdown files (book content)
**Testing**: Jest (frontend components), pytest (backend services)
**Target Platform**: Web application with Docusaurus frontend and FastAPI backend
**Project Type**: Web application (frontend + backend)
**Performance Goals**: <15 seconds for translation generation, 95% success rate for Claude Code Subagent requests
**Constraints**: Original content must remain immutable, translations must preserve technical accuracy, only authenticated users can access translation
**Scale/Scope**: Support up to 10,000 users with translation capability, handle chapters up to 10,000 words

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase Isolation Check
- [X] Only current phase features are being implemented
- [X] No future phase features are being implemented early
- [X] Previous phase is locked before starting current phase

### No Scope Creep Check
- [X] Features belong only to their assigned phase
- [X] No "small additions" from future phases
- [X] No refactors after phase lock

### AI-Friendly Structure Check
- [X] Clear specs exist before planning
- [X] Clear plans exist before implementation
- [X] Clear verification exists before locking

### Deterministic Execution Check
- [X] Every phase produces verifiable outputs
- [X] Ambiguity is resolved in Specify, not Implement

### Mandatory Phase Execution Lifecycle Check
- [X] Follows Specify → Plan → Implement → Verify → Lock sequence
- [X] No phase overlap allowed

### Locked Project Phases Check
- [X] Project phases completed in locked order
- [X] No skipping phases

## Project Structure

### Documentation (this feature)

```text
specs/005-translation-system/
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
│   │   ├── TranslationToggle.js      # Translation language toggle button
│   │   ├── TranslatedContent.js      # Component to display translated content
│   │   └── AuthProvider.js           # Authentication context (from Phase 3)
│   ├── pages/
│   │   └── DocPage.js               # Modified DocPage to include translation
│   ├── services/
│   │   └── translation.js           # Service to interact with translation API
│   └── css/
│       └── translation.css          # Styling for translation UI elements
└── static/
    └── docs/                        # Original book content (from Phase 1)

backend/
├── src/
│   ├── services/
│   │   └── translation.py           # Backend service for translation
│   ├── api/
│   │   └── translation.py           # API endpoints for translation
│   └── models/
│       └── translation.py           # Data models for translation session
└── tests/
    └── unit/
        └── test_translation.py      # Unit tests for translation service

agents/
├── claude-subagents/
│   ├── translation-agent.py         # Agent for handling translation tasks
│   └── agent-skills/
│       ├── terminology-preservation.py  # Skill to preserve technical terms
│       ├── code-block-protection.py     # Skill to protect code blocks
│       └── formatting-maintenance.py    # Skill to maintain formatting
```

**Structure Decision**: Web application structure with frontend (Docusaurus) components for UI and interaction, backend (FastAPI) services for translation logic, and agent directory for Claude Code Subagents and Agent Skills, following the architecture established in previous phases.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
