# Data Model: Translation System

## Translation Session Entity

### Fields
- **session_id**: UUID (Primary Key, auto-generated)
- **user_id**: UUID (Foreign Key to User.id from Phase 3)
- **chapter_id**: String (Identifier for the chapter being translated)
- **source_language**: String (Always "en" for English)
- **target_language**: String (Always "ur" for Urdu)
- **translation_state**: Enum ("active", "inactive") (Current state of translation)
- **created_at**: DateTime (Auto-generated timestamp)
- **updated_at**: DateTime (Auto-generated timestamp, updated on changes)

### Constraints
- session_id must be unique
- user_id must reference an existing User.id
- chapter_id must be a valid chapter identifier
- source_language must be "en"
- target_language must be "ur"
- Translation session expires after a defined period

### Validation Rules
- user_id: Required, must reference existing user
- chapter_id: Required, must be valid chapter identifier
- source_language: Required, must be "en"
- target_language: Required, must be "ur"

## Translated Content Entity

### Fields
- **content_id**: UUID (Primary Key, auto-generated)
- **session_id**: UUID (Foreign Key to TranslationSession.id)
- **original_content_id**: String (Reference to original content element)
- **original_text**: String (Original English text)
- **translated_text**: String (Translated Urdu text)
- **content_type**: Enum ("text", "heading", "code_block", "list_item", "table_cell")
- **preservation_flags**: JSON (Flags indicating preserved elements like technical terms)
- **created_at**: DateTime (Auto-generated timestamp)

### Constraints
- content_id must be unique
- session_id must reference an existing TranslationSession.id
- original_content_id must reference valid original content
- Translated content is tied to a specific session

### Validation Rules
- session_id: Required, must reference existing session
- original_content_id: Required, must reference valid content
- original_text: Required
- translated_text: Required
- content_type: Required, must be one of allowed values

## Relationships
- Translation Session (1) → (Many) Translated Content (One-to-many)
- User (1) → (Many) Translation Session (One-to-many)

## State Transitions
- Translation Session: Created when user clicks "Translate to Urdu", updated when activated/inactivated, deleted when session expires
- Translated Content: Created when AI generates translation for a session

## Indexes
- Translation Session.user_id: Index for fast user lookups
- Translation Session.chapter_id: Index for fast chapter lookups
- Translated Content.session_id: Index for fast session-based content retrieval