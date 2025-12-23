# API Contracts: AI-Driven Physical AI & Humanoid Robotics Book Platform

## Authentication APIs

### POST /api/auth/signup
**Description**: Create a new user account with background information
**Request**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe",
  "software_background": "intermediate",
  "hardware_background": "beginner",
  "ai_experience": "none"
}
```

**Response**:
- 201 Created: 
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "name": "John Doe",
  "created_at": "2025-12-24T10:00:00Z"
}
```
- 400 Bad Request: Validation errors
- 409 Conflict: Email already exists

### POST /api/auth/signin
**Description**: Authenticate user and return session token
**Request**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response**:
- 200 OK:
```json
{
  "token": "jwt-token-string",
  "user": {
    "id": "uuid-string",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```
- 401 Unauthorized: Invalid credentials

### POST /api/auth/signout
**Description**: End user session
**Response**:
- 200 OK: Session ended successfully

## Content APIs

### GET /api/content/modules
**Description**: Retrieve list of available modules
**Response**:
- 200 OK:
```json
[
  {
    "id": "uuid-string",
    "title": "The Robotic Nervous System",
    "description": "Introduction to ROS 2",
    "module_number": 1,
    "hero_image_url": "https://example.com/image.jpg",
    "is_published": true
  }
]
```

### GET /api/content/modules/{moduleId}/chapters
**Description**: Retrieve chapters for a specific module
**Response**:
- 200 OK:
```json
[
  {
    "id": "uuid-string",
    "title": "ROS 2 Basics",
    "slug": "ros2-basics",
    "chapter_number": 1,
    "is_published": true
  }
]
```

### GET /api/content/chapters/{chapterId}
**Description**: Retrieve content of a specific chapter
**Response**:
- 200 OK:
```json
{
  "id": "uuid-string",
  "title": "ROS 2 Basics",
  "slug": "ros2-basics",
  "content": "# ROS 2 Basics\n...",
  "module_id": "uuid-string",
  "chapter_number": 1,
  "is_published": true
}
```

## Personalization APIs

### GET /api/users/me/personalization
**Description**: Retrieve user's personalization settings
**Response**:
- 200 OK:
```json
{
  "content_depth": "intermediate",
  "preferred_language": "en",
  "learning_preferences": {
    "diagram_preference": "high",
    "math_preference": "low"
  }
}
```

### PUT /api/users/me/personalization
**Description**: Update user's personalization settings
**Request**:
```json
{
  "content_depth": "beginner",
  "preferred_language": "ur",
  "learning_preferences": {
    "diagram_preference": "high",
    "math_preference": "low"
  }
}
```

**Response**:
- 200 OK: Settings updated successfully

## Translation APIs

### POST /api/translate
**Description**: Translate content from one language to another
**Request**:
```json
{
  "content": "This is the content to translate",
  "source_language": "en",
  "target_language": "ur"
}
```

**Response**:
- 200 OK:
```json
{
  "translated_content": "یہ ترجمہ کرنے کا مواد ہے",
  "source_language": "en",
  "target_language": "ur"
}
```

## Chatbot APIs

### POST /api/chat/sessions
**Description**: Create a new chat session
**Request**:
```json
{
  "title": "New chat about ROS"
}
```

**Response**:
- 201 Created:
```json
{
  "id": "uuid-string",
  "title": "New chat about ROS",
  "created_at": "2025-12-24T10:00:00Z",
  "is_active": true
}
```

### POST /api/chat/sessions/{sessionId}/messages
**Description**: Send a message to the chatbot and receive a response
**Request**:
```json
{
  "content": "Explain ROS 2 nodes",
  "context": {
    "selected_text": "The text the user highlighted",
    "chapter_id": "uuid-string"
  }
}
```

**Response**:
- 201 Created:
```json
{
  "user_message": {
    "id": "uuid-string",
    "content": "Explain ROS 2 nodes",
    "sender_type": "user",
    "created_at": "2025-12-24T10:00:00Z"
  },
  "assistant_message": {
    "id": "uuid-string",
    "content": "ROS 2 nodes are...",
    "sender_type": "assistant",
    "created_at": "2025-12-24T10:00:05Z"
  }
}
```

### GET /api/chat/sessions
**Description**: Retrieve user's chat sessions
**Response**:
- 200 OK:
```json
[
  {
    "id": "uuid-string",
    "title": "New chat about ROS",
    "created_at": "2025-12-24T10:00:00Z",
    "updated_at": "2025-12-24T10:00:05Z",
    "is_active": true
  }
]
```

### GET /api/chat/sessions/{sessionId}/messages
**Description**: Retrieve messages in a specific chat session
**Response**:
- 200 OK:
```json
[
  {
    "id": "uuid-string",
    "content": "Explain ROS 2 nodes",
    "sender_type": "user",
    "created_at": "2025-12-24T10:00:00Z",
    "message_number": 1
  },
  {
    "id": "uuid-string",
    "content": "ROS 2 nodes are...",
    "sender_type": "assistant",
    "created_at": "2025-12-24T10:00:05Z",
    "message_number": 2
  }
]
```

## User Interaction APIs

### POST /api/users/me/interactions
**Description**: Record user interaction with content
**Request**:
```json
{
  "content_id": "uuid-string",
  "interaction_type": "view",
  "interaction_data": {
    "scroll_depth": 0.8,
    "time_spent": 120
  }
}
```

**Response**:
- 201 Created: Interaction recorded successfully