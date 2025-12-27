# Physical AI & Humanoid Robotics Book - Translation System

This repository contains the implementation of an AI-powered translation system that allows authenticated users to translate book content between English and Urdu while preserving technical accuracy.

## Features

- **User Authentication Required**: Translation functionality only available to logged-in users
- **Bidirectional Translation**: Support for English ↔ Urdu translation
- **Technical Term Preservation**: Critical technical terminology remains unchanged during translation
- **Code Block Protection**: Code examples are not translated to maintain functionality
- **Session-Based**: Translations are temporary and tied to user sessions
- **Visual Distinction**: Clear visual indication of translated vs. original content

## Architecture

The translation system consists of:

1. **Frontend Components**:
   - Translation toggle button
   - Content display with visual distinction
   - Authentication state management

2. **Backend Services**:
   - Translation API endpoints
   - Claude Code Subagent integration
   - JWT authentication validation
   - Session management

3. **AI Components**:
   - Claude Code Subagents for translation
   - Agent Skills for content processing
   - Deterministic, rule-based translation prompts

## Implementation Details

- **Frontend**: Docusaurus/React components for UI and interaction
- **Backend**: FastAPI services for translation logic and API endpoints
- **Authentication**: JWT-based authentication using existing Phase 3 infrastructure
- **AI Service**: Claude Code Subagents with specialized skills for technical content translation

## Files Included

- `/docusaurus` - Frontend implementation with translation UI components
- `/backend` - Backend services and API endpoints for translation
- `/agents` - Claude Code Subagent implementations and Agent Skills
- `/specs/005-translation-system` - Complete specification, plan, and task breakdown for the translation system

## Getting Started

1. Ensure you have completed Phases 1-4 of the project (Book Foundation, AI Chatbot, Authentication, Personalization)
2. Set up the required environment variables for Claude API access
3. Install dependencies for both frontend and backend
4. Start both servers to enable the translation functionality

## Security & Compliance

- All translation endpoints require JWT authentication
- Original content remains immutable
- User sessions are validated before translation access
- Technical accuracy is preserved during translation