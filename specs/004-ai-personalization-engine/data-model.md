# Data Model: AI-Powered Content Personalization

## Personalization Session Entity

### Fields
- **session_id**: UUID (Primary Key, auto-generated)
- **user_id**: UUID (Foreign Key to User.id from Phase 3)
- **chapter_id**: String (Identifier for the chapter being personalized)
- **user_profile**: JSON (Software and hardware background from user profile)
- **personalization_state**: Enum ("active", "inactive") (Current state of personalization)
- **created_at**: DateTime (Auto-generated timestamp)
- **updated_at**: DateTime (Auto-generated timestamp, updated on changes)

### Constraints
- session_id must be unique
- user_id must reference an existing User.id
- chapter_id must be a valid chapter identifier
- Personalization session expires after a defined period

### Validation Rules
- user_id: Required, must reference existing user
- chapter_id: Required, must be valid chapter identifier
- user_profile: Required, must contain software and hardware background

## Personalized Content Entity

### Fields
- **content_id**: UUID (Primary Key, auto-generated)
- **session_id**: UUID (Foreign Key to Personalization Session.id)
- **original_content_id**: String (Reference to original content)
- **personalized_text**: String (AI-generated personalized content)
- **personalization_type**: Enum ("explanation", "example", "difficulty-adjustment")
- **user_background_level**: Enum ("beginner", "intermediate", "advanced")
- **created_at**: DateTime (Auto-generated timestamp)

### Constraints
- content_id must be unique
- session_id must reference an existing Personalization Session
- original_content_id must reference valid original content
- Personalized content is tied to a specific session

### Validation Rules
- session_id: Required, must reference existing session
- original_content_id: Required, must reference valid content
- personalized_text: Required, minimum length validation
- personalization_type: Required, must be one of allowed values

## Relationships
- Personalization Session (1) → (Many) Personalized Content (One-to-many)
- User (1) → (Many) Personalization Session (One-to-many)

## State Transitions
- Personalization Session: Created when user clicks "Personalize Content", updated when activated/inactivated, deleted when session expires
- Personalized Content: Created when AI generates content for a session

## Indexes
- Personalization Session.user_id: Index for fast user lookups
- Personalization Session.chapter_id: Index for fast chapter lookups
- Personalized Content.session_id: Index for fast session-based content retrieval