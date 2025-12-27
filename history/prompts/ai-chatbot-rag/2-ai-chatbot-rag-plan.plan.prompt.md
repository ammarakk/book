---
id: 2
title: ai-chatbot-rag-plan
stage: plan
date: 2025-01-04
surface: agent
model: gpt-4
feature: ai-chatbot-rag
branch: 002-ai-chatbot-rag
user: User
command: /sp.plan
labels: ["plan", "ai", "chatbot", "rag", "docusaurus", "book", "robotics"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\\Users\\User\\Documents\\books\\specs\\002-ai-chatbot-rag\\plan.md
 - C:\\Users\\User\\Documents\\books\\specs\\002-ai-chatbot-rag\\research.md
 - C:\\Users\\User\\Documents\\books\\specs\\002-ai-chatbot-rag\\data-model.md
 - C:\\Users\\User\\Documents\\books\\specs\\002-ai-chatbot-rag\\quickstart.md
 - C:\\Users\\User\\Documents\\books\\specs\\002-ai-chatbot-rag\\contracts\\openapi.yaml
tests:
 - none
---

## Prompt

```
/sp.plan /sp.plan Phase 2 – AI Chatbot (RAG System)

Phase Objective:
Design and integrate an AI-powered Retrieval-Augmented Generation (RAG) chatbot into the Physical AI & Humanoid Robotics book that can accurately answer questions using only the book's content.

This phase focuses on SYSTEM DESIGN and EXECUTION ORDER.
No authentication, personalization, or translation logic is included.

--------------------------------------------------
PHASE 2 EXECUTION STRATEGY
--------------------------------------------------

Execution Model:
- Spec-driven
- Backend-first
- Deterministic
- UI-light but production-ready

The chatbot must be:
- Embedded inside the Docusaurus book
- Content-grounded (no hallucination)
- Context-aware
- Selective-text aware
- Phase-isolated

--------------------------------------------------
SYSTEM ARCHITECTURE
--------------------------------------------------

1. High-Level Flow

User (Book UI)
→ Chat Widget (React)
→ FastAPI Backend
→ RAG Pipeline
→ Ollama LLM
→ Response
→ UI Render

--------------------------------------------------

2. Core Components

A. Frontend (Docusaurus)
- Floating chatbot widget
- Animated robot-style icon
- Expand / collapse behavior
- Input box + message history
- Optional "Ask about selected text" mode
- Read-only integration (no login)

B. Backend (FastAPI)
- REST API for chat requests
- Endpoints:
  - POST /chat
  - POST /chat/selection
- Request validation
- Rate-limiting ready (not enforced yet)

C. RAG Pipeline
- Document chunking (book markdown)
- Embedding generation
- Vector similarity search
- Context injection into prompt
- Strict content-bound answering

D. LLM
- Ollama (local or server-hosted)
- Model selectable via environment variable
- No cloud LLM dependency

E. Data Stores
- Qdrant Cloud (Free Tier)
  - Stores embeddings
  - Used only for retrieval
- Neon Serverless Postgres
  - Stores document metadata
  - Chunk IDs, source mapping

--------------------------------------------------
RAG DESIGN DETAILS
--------------------------------------------------

1. Data Ingestion
- Parse Docusaurus markdown files
- Split content into semantic chunks
- Attach metadata:
  - Module
  - Chapter
  - Section
  - Source URL

2. Embeddings
- Generated once (offline step)
- Stored in Qdrant
- Chunk size fixed and deterministic

3. Retrieval
- Top-K similarity search
- Metadata-filtered retrieval
- No cross-document leakage

4. Prompt Construction
System Prompt:
- You are a book assistant
- You may ONLY answer from provided context
- If answer is not in context → say "Not found in book"

--------------------------------------------------
SELECTED-TEXT MODE
--------------------------------------------------

If user selects text:
- Only selected text is embedded
- No global search allowed
- Answer must reference selection only

--------------------------------------------------
UI PLAN
--------------------------------------------------

Chat Widget:
- Floating bottom-right
- Neon robotic styling
- Smooth open/close animation
- Robot icon (real-world humanoid inspired)

States:
- Idle
- Loading
- Responding
- Error (context not found)

--------------------------------------------------
CONFIGURATION & ENVIRONMENT
--------------------------------------------------

Environment Variables:
- OLLAMA_MODEL
- OLLAMA_BASE_URL
- QDRANT_URL
- QDRANT_API_KEY
- NEON_DATABASE_URL

No secrets hardcoded.

--------------------------------------------------
OUT OF SCOPE (STRICT)
--------------------------------------------------

- User authentication
- Signup / Signin
- User profiles
- Personalization
- Translation
- Payment / limits
- Analytics

--------------------------------------------------
PHASE COMPLETION CRITERIA
--------------------------------------------------

Phase 2 is COMPLETE when:
- Chatbot is visible inside book UI
- Chat answers ONLY from book content
- Selected-text-only answering works
- Ollama LLM responds correctly
- Qdrant retrieval is accurate
- Backend is stable
- No auth or personalization exists

--------------------------------------------------
PHASE LOCK RULE
--------------------------------------------------

Once Phase 2 is locked:
- No chatbot logic changes
- No UI redesign
- No backend refactors
- Phase 3 may begin ONLY after lock

--------------------------------------------------
TRANSITION TO PHASE 3
--------------------------------------------------

Next Phase:
Phase 3 – Authentication & User Profiles

Handoff Artifacts:
- Stable FastAPI backend
- RAG pipeline ready
- Chat UI embedded
- Vector DB populated
```

## Response snapshot

Successfully executed the implementation planning workflow for Phase 2 – AI Chatbot (RAG System). The following artifacts were created:

1. Implementation Plan (plan.md): Complete plan with technical context, constitution checks, and project structure
2. Research Summary (research.md): Addressing NEEDS CLARIFICATION items and technology decisions
3. Data Model (data-model.md): Defining entities and database schemas for the RAG system
4. API Contracts (contracts/openapi.yaml): OpenAPI specification for the chatbot API
5. Quickstart Guide (quickstart.md): Instructions for setting up and running the system

The plan includes:
- Python 3.11+ for backend services
- FastAPI for backend framework
- Docusaurus and React for frontend
- Ollama for LLM runtime
- Qdrant Cloud for vector storage
- Neon Serverless PostgreSQL for metadata
- All constitution checks passed

The agent context was updated with the new technology stack information.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for Phase 2 of the Physical AI & Humanoid Robotics Book project
- 🧪 Tests: No tests required for this planning task
- 📁 Files: 5 files created (plan.md, research.md, data-model.md, quickstart.md, contracts/openapi.yaml)
- 🔁 Next prompts: Ready for /sp.tasks to break the plan into tasks
- 🧠 Reflection: The plan properly maintains phase isolation as required by the constitution

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for this documentation task
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed with /sp.tasks to create task breakdown