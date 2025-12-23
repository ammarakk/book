# Data Model: AI-Driven Physical AI & Humanoid Robotics Book Platform

## Entities & Relationships

### 1. User Entity
- **Fields**:
  - id (UUID, primary key)
  - email (string, unique, required)
  - password_hash (string, required)
  - name (string, required)
  - software_background (string, optional)
  - hardware_background (string, optional)
  - ai_experience (string, optional)
  - created_at (timestamp, required)
  - updated_at (timestamp, required)
  - last_login_at (timestamp, optional)
  - is_active (boolean, default: true)
  - preferences (JSON, optional)

- **Relationships**:
  - One-to-many with UserPersonalizationSettings
  - One-to-many with ChatSession
  - One-to-many with UserContentInteraction

- **Validation Rules**:
  - Email must be valid email format
  - Password must meet complexity requirements
  - Name must be between 2-100 characters

### 2. BookContent Entity
- **Fields**:
  - id (UUID, primary key)
  - title (string, required)
  - slug (string, unique, required)
  - content (text/markdown, required)
  - content_urdu (text/markdown, optional)
  - module_id (UUID, required)
  - chapter_number (integer, required)
  - type (enum: 'module', 'chapter', 'section', required)
  - parent_id (UUID, optional, self-referencing)
  - created_at (timestamp, required)
  - updated_at (timestamp, required)
  - is_published (boolean, default: true)
  - metadata (JSON, optional)

- **Relationships**:
  - Many-to-one with Module
  - One-to-many with UserContentInteraction
  - One-to-many with ContentTranslation

- **Validation Rules**:
  - Title must be between 5-200 characters
  - Content must be valid markdown
  - Chapter number must be positive

### 3. Module Entity
- **Fields**:
  - id (UUID, primary key)
  - title (string, required)
  - description (text, optional)
  - module_number (integer, required)
  - hero_image_url (string, optional)
  - created_at (timestamp, required)
  - updated_at (timestamp, required)
  - is_published (boolean, default: true)
  - metadata (JSON, optional)

- **Relationships**:
  - One-to-many with BookContent
  - One-to-many with ModuleInteraction

- **Validation Rules**:
  - Title must be between 5-200 characters
  - Module number must be positive

### 4. UserPersonalizationSettings Entity
- **Fields**:
  - id (UUID, primary key)
  - user_id (UUID, required, foreign key to User)
  - content_depth (enum: 'beginner', 'intermediate', 'advanced', default: 'intermediate')
  - preferred_language (enum: 'en', 'ur', default: 'en')
  - learning_preferences (JSON, optional)
  - created_at (timestamp, required)
  - updated_at (timestamp, required)

- **Relationships**:
  - Many-to-one with User
  - One-to-many with PersonalizedContent

- **Validation Rules**:
  - User ID must reference an existing user
  - Content depth must be one of the allowed values

### 5. ChatSession Entity
- **Fields**:
  - id (UUID, primary key)
  - user_id (UUID, required, foreign key to User, nullable for anonymous)
  - title (string, required)
  - created_at (timestamp, required)
  - updated_at (timestamp, required)
  - is_active (boolean, default: true)
  - metadata (JSON, optional)

- **Relationships**:
  - Many-to-one with User
  - One-to-many with ChatMessage

- **Validation Rules**:
  - Title must be between 5-100 characters
  - Either user_id must be provided or session is anonymous

### 6. ChatMessage Entity
- **Fields**:
  - id (UUID, primary key)
  - chat_session_id (UUID, required, foreign key to ChatSession)
  - sender_type (enum: 'user', 'assistant', required)
  - content (text, required)
  - context (JSON, optional)
  - created_at (timestamp, required)
  - message_number (integer, required)

- **Relationships**:
  - Many-to-one with ChatSession

- **Validation Rules**:
  - Content must be between 1-5000 characters
  - Message number must be sequential within session

### 7. UserContentInteraction Entity
- **Fields**:
  - id (UUID, primary key)
  - user_id (UUID, required, foreign key to User)
  - content_id (UUID, required, foreign key to BookContent)
  - interaction_type (enum: 'view', 'personalize', 'translate', 'bookmark', required)
  - created_at (timestamp, required)
  - interaction_data (JSON, optional)

- **Relationships**:
  - Many-to-one with User
  - Many-to-one with BookContent

- **Validation Rules**:
  - User ID must reference an existing user
  - Content ID must reference an existing content item

### 8. ContentTranslation Entity
- **Fields**:
  - id (UUID, primary key)
  - content_id (UUID, required, foreign key to BookContent)
  - source_language (enum: 'en', required)
  - target_language (enum: 'ur', required)
  - translated_content (text, required)
  - created_at (timestamp, required)
  - updated_at (timestamp, required)
  - is_approved (boolean, default: false)

- **Relationships**:
  - Many-to-one with BookContent

- **Validation Rules**:
  - Source and target languages must be different
  - Content ID must reference an existing content item

## State Transitions

### User Entity
- Created → Active (after email verification)
- Active → Inactive (user deactivation)
- Inactive → Active (user reactivation)

### ChatSession Entity
- Created → Active (when first message is sent)
- Active → Inactive (after period of inactivity)
- Inactive → Archived (after extended inactivity)

## Database Indexes

### User Entity
- Index on email (for authentication)
- Index on created_at (for user analytics)

### BookContent Entity
- Index on slug (for content retrieval)
- Index on module_id (for module content queries)
- Index on type and is_published (for content listing)

### ChatSession Entity
- Index on user_id (for user's chat history)
- Index on created_at (for chronological ordering)

### UserContentInteraction Entity
- Index on user_id and content_id (for interaction tracking)
- Index on interaction_type (for analytics)

## Relationships Summary

```
User 1----* UserPersonalizationSettings
User 1----* ChatSession
User 1----* UserContentInteraction

Module 1----* BookContent
BookContent 1----* UserContentInteraction
BookContent 1----* ContentTranslation

ChatSession 1----* ChatMessage
```