# Translation API Contracts

## Translation Endpoints

### POST /api/translate/request
**Description**: Request translation of a specific chapter from English to Urdu

**Request** (requires authentication):
```json
{
  "chapter_id": "chapter-1-introduction-to-ros",
  "target_language": "ur"
}
```

**Response (200 OK)**:
```json
{
  "session_id": "uuid-string",
  "chapter_id": "chapter-1-introduction-to-ros",
  "source_language": "en",
  "target_language": "ur",
  "translated_content": [
    {
      "content_id": "uuid-string",
      "original_content_id": "original-paragraph-123",
      "original_text": "In robotics, the Robot Operating System (ROS) provides a framework for writing robot software...",
      "translated_text": "روبوٹکس میں، روبوٹ آپریٹنگ سسٹم (ROS) روبوٹ سافٹ ویئر لکھنے کے لیے ایک فریم ورک فراہم کرتا ہے...",
      "content_type": "text",
      "preservation_flags": {
        "technical_terms": ["ROS"],
        "code_elements": []
      }
    },
    {
      "content_id": "uuid-string",
      "original_content_id": "original-code-block-456",
      "original_text": "// This is a ROS publisher example\nros::Publisher pub = n.advertise<std_msgs::String>(\"chatter\", 1000);",
      "translated_text": "// یہ ایک ROS پبلشر کی مثال ہے\nros::Publisher pub = n.advertise<std_msgs::String>(\"chatter\", 1000);",
      "content_type": "code_block",
      "preservation_flags": {
        "technical_terms": [],
        "code_elements": ["ros::Publisher pub = n.advertise<std_msgs::String>(\"chatter\", 1000);"]
      }
    }
  ],
  "status": "completed"
}
```

**Validation**:
- User must be authenticated
- Chapter ID must be valid
- Target language must be "ur"

**Errors**:
- 401: User not authenticated
- 400: Invalid input data
- 500: Claude Code Subagent unavailable

### GET /api/translate/session/{session_id}
**Description**: Retrieve translated content for an existing translation session

**Request**: (No body required, uses authentication header)

**Response (200 OK)**:
```json
{
  "session_id": "uuid-string",
  "chapter_id": "chapter-1-introduction-to-ros",
  "source_language": "en",
  "target_language": "ur",
  "translated_content": [
    {
      "content_id": "uuid-string",
      "original_content_id": "original-paragraph-123",
      "original_text": "In robotics...",
      "translated_text": "روبوٹکس میں...",
      "content_type": "text",
      "preservation_flags": {
        "technical_terms": ["ROS"],
        "code_elements": []
      }
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

### Subagent: TranslationAgent
**Purpose**: Generate accurate English-Urdu translations while preserving technical content
**Input**: Original content, target language, preservation requirements
**Output**: Translated content with technical elements preserved

### Agent Skills

#### Skill: TechnicalTermPreservation
**Purpose**: Ensure technical terminology remains unchanged during translation
**Input**: Content with potential technical terms
**Output**: Content with technical terms marked for preservation

#### Skill: CodeBlockProtection
**Purpose**: Identify and protect code blocks from translation
**Input**: Content with potential code blocks
**Output**: Content with code blocks marked for preservation

#### Skill: FormattingMaintenance
**Purpose**: Preserve document structure and formatting during translation
**Input**: Content with formatting elements
**Output**: Content with formatting structure maintained