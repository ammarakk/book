<!-- SYNC IMPACT REPORT
Version change: N/A (initial version) → 1.0.0
Modified principles: N/A
Added sections: All principles and sections from user input
Removed sections: N/A
Templates requiring updates: N/A
Follow-up TODOs: [RATIFICATION_DATE] marked as TODO since original date unknown
-->

# Physical AI & Humanoid Robotics Constitution

## Core Principles

### Spec-First Development
All work must originate from `/sp.constitution`, `/sp.specify`, `/sp.plan`, and `/sp.task`. No code, content, or architecture decisions are made outside the spec flow. AI agents must strictly follow the defined specs.

### AI as a Collaborative Engineer
Claude Code acts as the primary reasoning and orchestration agent. Qwen and Gemini are used as free-tier execution and content agents. Reusable intelligence is created through subagents and agent skills.

### Educational Accuracy & Currency
Content must be technically accurate, up-to-date, and industry-aligned. Robotics, AI, and simulation tools must reflect current best practices. Sources and references must be clearly linked in the book body and footer.

### Book Architecture & Platform
Docusaurus is the official documentation and book framework with a Neon Robotics / Futuristic Theme. The layout must include header, body, and footer with navigation, auth state, chapters, modules, interactive elements, references, and links.

### Authentication & Personalization
Signup and Signin implemented using Better Auth with Neon Serverless PostgreSQL. Users answer background questions during signup, and profile data personalizes chapter content and adjusts explanations.

### Embedded RAG Chatbot System
The chatbot answers questions related to book content with whole-book, chapter-specific, and user-selected text context. Uses Neon-compatible chat UI, Ollama LLM, FastAPI backend, Qdrant Cloud vector DB, and Neon Postgres for chat history.

## Functional Requirements
Includes chapter-level personalization with 'Personalize Content' button for logged-in users, and translation system with 'Translate to Urdu' button that preserves technical meaning while keeping English as default.

## Reusable Intelligence & Deployment
Defines Claude Code subagents and reusable agent skills. Requires deterministic, versioned, and auditable agent outputs. Codebase hosted on GitHub, deployed via GitHub Pages with cloud-compatible backend services and local development support.

## Governance
The constitution supersedes all other practices. All work originates from spec flow. Amendments require documentation, approval, and migration plan. All PRs/reviews must verify compliance.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Original adoption date unknown | **Last Amended**: 2025-12-24