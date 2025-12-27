# Personalization Engine API Contracts

## Personalization Endpoints

### POST /api/personalize/request
**Description**: Request personalized content for a specific chapter based on user profile

**Request** (requires authentication):
```json
{
  "chapter_id": "chapter-1-introduction-to-ros",
  "user_background": {
    "software_background": "beginner",
    "hardware_background": "none"
  }
}
```

**Response (200 OK)**:
```json
{
  "session_id": "uuid-string",
  "chapter_id": "chapter-1-introduction-to-ros",
  "personalized_content": [
    {
      "content_id": "uuid-string",
      "original_content_id": "original-paragraph-123",
      "personalized_text": "As a beginner, think of ROS as a toolkit that helps different parts of your robot communicate with each other...",
      "personalization_type": "explanation",
      "user_background_level": "beginner"
    },
    {
      "content_id": "uuid-string",
      "original_content_id": "original-code-block-456",
      "personalized_text": "For beginners, this code is setting up a basic publisher that sends messages to other parts of your robot...",
      "personalization_type": "explanation",
      "user_background_level": "beginner"
    }
  ]
}
```

**Validation**:
- User must be authenticated
- Chapter ID must be valid
- User background must match available profile data

**Errors**:
- 401: User not authenticated
- 400: Invalid input data
- 500: Claude Code Subagent unavailable

### GET /api/personalize/session/{session_id}
**Description**: Retrieve personalized content for an existing personalization session

**Request**: (No body required, uses authentication header)

**Response (200 OK)**:
```json
{
  "session_id": "uuid-string",
  "chapter_id": "chapter-1-introduction-to-ros",
  "personalized_content": [
    {
      "content_id": "uuid-string",
      "original_content_id": "original-paragraph-123",
      "personalized_text": "As a beginner, think of ROS as a toolkit that helps different parts of your robot communicate with each other...",
      "personalization_type": "explanation",
      "user_background_level": "beginner"
    }
  ],
  "status": "active"
}
```

**Errors**:
- 401: User not authenticated
- 404: Session not found
- 410: Session expired

## Claude Code Subagent Integration

### Subagent: BeginnerAgent
**Purpose**: Generate simplified explanations and examples for users with beginner-level backgrounds
**Input**: Original content, user profile with beginner background
**Output**: Simplified explanations, basic examples, analogies

### Subagent: IntermediateAgent
**Purpose**: Generate moderately detailed explanations for users with intermediate backgrounds
**Input**: Original content, user profile with intermediate background
**Output**: Moderate explanations, relevant examples, moderate technical detail

### Subagent: AdvancedAgent
**Purpose**: Generate detailed, technical explanations for users with advanced backgrounds
**Input**: Original content, user profile with advanced background
**Output**: Advanced explanations, complex examples, detailed technical content

## Agent Skills

### Skill: ContentSimplification
**Purpose**: Simplify complex concepts for beginner users
**Input**: Complex technical content
**Output**: Simplified explanations with analogies

### Skill: TechnicalElaboration
**Purpose**: Add technical depth for advanced users
**Input**: Basic content
**Output**: Detailed technical explanations

### Skill: TerminologyValidation
**Purpose**: Ensure technical terms remain unchanged in personalized content
**Input**: Personalized content
**Output**: Content with verified technical terms