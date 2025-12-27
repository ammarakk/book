# AI-Powered Translation System (English ↔ Urdu)

This directory contains the implementation for the AI-powered translation system that allows authenticated users to translate book content between English and Urdu while preserving technical accuracy.

## Architecture

The translation system consists of:

1. **Frontend Components**:
   - `TranslationToggle.js`: Button that triggers translation functionality
   - `TranslatedContent.js`: Component that displays translated content with visual distinction
   - `translation.css`: Styling for translation UI elements

2. **Backend Services**:
   - `api/translation.py`: API endpoints for translation requests
   - `services/translation.py`: Core translation logic and session management
   - `models/translation.py`: Data models for translation sessions and content

3. **AI Components**:
   - `agents/claude-subagents/`: Claude Code Subagent framework for translation
   - `agents/claude-subagents/agent-skills/`: Specialized skills for content processing

## How It Works

1. When a logged-in user clicks the "Translate to Urdu" button, a request is sent to the backend
2. The backend verifies the user's authentication using JWT
3. The Claude Code Subagent generates a translation of the content while preserving:
   - Technical terminology (ROS 2, SLAM, URDF, Isaac Sim, etc.)
   - Code blocks (which remain in English)
   - Headings, lists, tables, and formatting
4. The translated content is returned to the frontend with metadata
5. The frontend displays the translated content with clear visual distinction from original content

## Security

- All translation endpoints require JWT authentication
- Users can only access translation sessions they created
- Original content remains immutable
- Rate limiting should be implemented in production

## Extensibility

While currently supporting English ↔ Urdu translation, the architecture allows for adding additional language pairs by:
1. Creating new agent configurations for the target language
2. Updating the language validation logic
3. Adding appropriate UI labels for the new language

## Files

- `api-documentation.md`: Complete API documentation for translation endpoints
- `verification-checklist.md`: Checklist to verify Phase 3 completion criteria