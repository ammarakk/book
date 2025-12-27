# Personalization Engine Documentation

## Overview
The Personalization Engine is an AI-driven system that adapts chapter-level explanations based on the logged-in user's background (software and hardware experience). The system uses Claude Code Subagents to generate personalized content that enhances understanding while preserving the original book content.

## Architecture
The system consists of:
- Frontend components (Docusaurus/React)
- Backend services (FastAPI)
- Claude Code Subagents for content generation
- Agent Skills for specialized processing

## Components

### Frontend Components
- `PersonalizeButton`: Shows/hides based on authentication state
- `PersonalizedContent`: Displays personalized content with visual distinction
- `personalizationService`: Handles API communication

### Backend Services
- `personalization.py`: Core personalization logic
- API endpoints for requesting and retrieving personalized content
- Claude Code Subagent integration

## Claude Code Subagents
- `BeginnerAgent`: Generates simplified explanations for beginners
- `IntermediateAgent`: Generates moderately detailed explanations
- `AdvancedAgent`: Generates detailed, technical explanations

## Agent Skills
- `ContentSimplificationSkill`: Simplifies complex concepts
- `TechnicalElaborationSkill`: Adds technical depth
- `TerminologyValidationSkill`: Ensures technical terms remain unchanged

## API Endpoints
- `POST /api/personalize/request`: Request personalized content
- `GET /api/personalize/session/{session_id}`: Retrieve personalized content for a session

## Security
- JWT-based authentication required for all endpoints
- Session-based personalization (not permanent)
- User sessions are tied to specific user IDs