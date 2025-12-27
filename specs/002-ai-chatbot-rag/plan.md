# Implementation Plan: Phase 2 – AI Chatbot (RAG System)

**Branch**: `002-ai-chatbot-rag` | **Date**: 2025-01-04 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/002-ai-chatbot-rag/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the implementation of Phase 2 – AI Chatbot (RAG System) for the Physical AI & Humanoid Robotics book. The primary requirement is to create an AI-powered chatbot that can answer user questions using only the book's content, with strict grounding to prevent hallucinations.

The technical approach involves:
- Building a FastAPI backend to handle chat requests and manage the RAG pipeline
- Using Ollama as the local LLM runtime for content generation
- Storing document embeddings in Qdrant Cloud vector store for efficient retrieval
- Storing document metadata in Neon Serverless PostgreSQL
- Creating a React-based chat widget embedded in the Docusaurus book UI
- Implementing two modes: global (full book context) and selection (selected text only)

This implementation strictly follows the project constitution by maintaining phase isolation and avoiding any features from future phases (authentication, personalization, translation).

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.11+ for backend services, JavaScript/TypeScript for frontend
**Primary Dependencies**: FastAPI (backend), Docusaurus (frontend), React (UI components), Ollama (LLM runtime)
**Storage**: Qdrant Cloud (vector store for embeddings), Neon Serverless PostgreSQL (metadata storage)
**Testing**: pytest for backend unit/integration tests, Jest for frontend component tests (NEEDS CLARIFICATION: specific testing approach for RAG functionality)
**Target Platform**: Web browser (Chrome, Firefox, Safari, Edge) - responsive design for desktop and mobile
**Project Type**: Hybrid application (frontend Docusaurus site with backend FastAPI services)
**Performance Goals**: Query response time < 5 seconds, embedding generation time < 10 seconds, 99% uptime for chat service
**Constraints**: No external web access for LLM queries, content must be grounded in book materials only, no user data persistence
**Scale/Scope**: Single book with 5 modules, expected to handle 100 concurrent users during peak times

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

*Post-design evaluation: All checks remain valid after Phase 2 design completion.*

## Project Structure

### Documentation (this feature)

```text
specs/002-ai-chatbot-rag/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── openapi.yaml     # API contracts specification
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# Backend service structure for the RAG chatbot
backend/
├── main.py                 # FastAPI application entry point
├── config.py               # Configuration settings (API keys, model settings)
├── models/
│   ├── chat.py             # Chat request/response models
│   ├── embeddings.py       # Embedding models
│   └── database.py         # Database models
├── services/
│   ├── rag_service.py      # Core RAG pipeline logic
│   ├── embedding_service.py # Embedding generation and management
│   ├── chat_service.py     # Chat interaction logic
│   └── document_service.py # Document processing and retrieval
├── api/
│   ├── deps.py             # Dependency injection
│   ├── routes/
│   │   ├── chat.py         # Chat endpoints
│   │   └── health.py       # Health check endpoints
│   └── v1/                 # API versioning
├── utils/
│   ├── validators.py       # Input validation utilities
│   └── helpers.py          # General helper functions
├── tests/
│   ├── conftest.py         # Test configuration
│   ├── test_chat.py        # Chat functionality tests
│   ├── test_rag.py         # RAG pipeline tests
│   └── integration/        # Integration tests
└── requirements.txt        # Python dependencies

# Docusaurus book with embedded chatbot
docusaurus/
├── physical-ai-book/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatWidget/     # Chatbot UI component
│   │   │   │   ├── ChatWindow.jsx
│   │   │   │   ├── ChatMessage.jsx
│   │   │   │   ├── ChatInput.jsx
│   │   │   │   └── FloatingButton.jsx
│   │   │   ├── BookContent/    # Book-specific components
│   │   │   └── utils/          # Utility functions
│   │   ├── css/
│   │   │   └── chat-widget.css # Chatbot styling
│   │   └── pages/
│   ├── docs/                   # Book content (from Phase 1)
│   ├── static/                 # Static assets
│   ├── docusaurus.config.js    # Docusaurus configuration
│   ├── sidebars.js             # Navigation configuration
│   └── package.json            # Node.js dependencies
```

**Structure Decision**: The architecture separates the RAG backend service from the Docusaurus frontend to maintain clear boundaries between AI processing and content presentation. The chatbot UI is embedded directly in the book using React components that communicate with the backend API.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
