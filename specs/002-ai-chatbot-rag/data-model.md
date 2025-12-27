# Data Model: Phase 2 – AI Chatbot (RAG System)

## Overview
This document defines the data models for the AI Chatbot (RAG System) that will be integrated into the Physical AI & Humanoid Robotics book. The system involves both frontend UI state and backend data for the RAG pipeline.

## Core Entities

### ChatQuery
**Description**: Represents a user's question submitted to the chatbot system

**Fields**:
- id: String (unique identifier for the query)
- sessionId: String (reference to the chat session)
- questionText: String (the actual question text from the user)
- contextMode: String (either "global" for full book context or "selection" for selected text only)
- selectedText: String (optional text that was selected when contextMode is "selection")
- timestamp: DateTime (when the query was submitted)
- userId: String (optional user identifier if available)

**Validation**:
- id must be unique across all queries
- questionText must not be empty
- contextMode must be either "global" or "selection"
- if contextMode is "selection", selectedText must not be empty

### DocumentChunk
**Description**: A segment of book content that has been processed for vector storage

**Fields**:
- id: String (unique identifier for the chunk)
- content: String (the actual text content of the chunk)
- sourceModule: String (which module this chunk belongs to, e.g., "module-1-robotic-nervous-system")
- sourceChapter: String (which chapter this chunk belongs to)
- sourceSection: String (which section within the chapter)
- sourceUrl: String (URL to the original document location)
- embeddingId: String (ID in the vector database for this chunk's embedding)
- metadata: Object (additional metadata like page numbers, headings, etc.)

**Validation**:
- id must be unique across all chunks
- content must not be empty
- sourceModule, sourceChapter, and sourceUrl must be valid references
- embeddingId must correspond to an entry in the vector database

### VectorEmbedding
**Description**: Numerical representation of document content for similarity matching

**Fields**:
- id: String (unique identifier for the embedding)
- documentChunkId: String (reference to the document chunk this embedding represents)
- embeddingVector: Array<Float> (the actual numerical vector representation)
- createdAt: DateTime (when the embedding was generated)

**Validation**:
- id must be unique across all embeddings
- documentChunkId must reference an existing document chunk
- embeddingVector must have the correct dimensionality for the model used

### ChatResponse
**Description**: The system's answer to a user's query

**Fields**:
- id: String (unique identifier for the response)
- queryId: String (reference to the original query)
- answerText: String (the generated answer text)
- sourceChunks: Array<String> (IDs of the document chunks that informed the answer)
- confidenceLevel: Float (confidence score between 0 and 1)
- retrievalMetadata: Object (metadata about which chunks were retrieved and used)
- timestamp: DateTime (when the response was generated)

**Validation**:
- id must be unique across all responses
- queryId must reference an existing query
- answerText must not be empty
- confidenceLevel must be between 0 and 1

### DocumentMetadata
**Description**: Information about book content stored in the database

**Fields**:
- id: String (unique identifier for the metadata record)
- documentId: String (identifier for the original document)
- sourceFilePath: String (path to the original markdown file)
- moduleName: String (which module this document belongs to)
- chapterName: String (which chapter this document belongs to)
- sectionName: String (which section within the chapter)
- contentHash: String (hash of the content to detect changes)
- createdAt: DateTime (when this metadata was created)
- updatedAt: DateTime (when this metadata was last updated)

**Validation**:
- id must be unique across all metadata records
- documentId must be unique for each document
- sourceFilePath must be a valid path
- contentHash must be a valid SHA hash

### ChatSession
**Description**: A user's interaction session with the chatbot

**Fields**:
- id: String (unique identifier for the session)
- userId: String (optional user identifier)
- createdAt: DateTime (when the session was started)
- lastActivityAt: DateTime (when the last query was made in this session)
- isActive: Boolean (whether the session is currently active)

**Validation**:
- id must be unique across all sessions
- createdAt must be before lastActivityAt

## Database Schemas

### Neon PostgreSQL Schema
The following tables will be created in the Neon Serverless PostgreSQL database:

```sql
CREATE TABLE document_metadata (
  id VARCHAR(255) PRIMARY KEY,
  document_id VARCHAR(255) UNIQUE NOT NULL,
  source_file_path TEXT NOT NULL,
  module_name VARCHAR(255) NOT NULL,
  chapter_name VARCHAR(255) NOT NULL,
  section_name VARCHAR(255),
  content_hash VARCHAR(64) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chat_sessions (
  id VARCHAR(255) PRIMARY KEY,
  user_id VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_activity_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE chat_queries (
  id VARCHAR(255) PRIMARY KEY,
  session_id VARCHAR(255) REFERENCES chat_sessions(id),
  question_text TEXT NOT NULL,
  context_mode VARCHAR(20) CHECK (context_mode IN ('global', 'selection')) NOT NULL,
  selected_text TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chat_responses (
  id VARCHAR(255) PRIMARY KEY,
  query_id VARCHAR(255) REFERENCES chat_queries(id),
  answer_text TEXT NOT NULL,
  source_chunks TEXT[], -- Array of document chunk IDs
  confidence_level DECIMAL(3, 2) CHECK (confidence_level >= 0 AND confidence_level <= 1),
  retrieval_metadata JSONB,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_document_metadata_module ON document_metadata(module_name);
CREATE INDEX idx_chat_sessions_user ON chat_sessions(user_id);
CREATE INDEX idx_chat_queries_session ON chat_queries(session_id);
CREATE INDEX idx_chat_queries_timestamp ON chat_queries(timestamp);
CREATE INDEX idx_chat_responses_query ON chat_responses(query_id);
```

### Qdrant Vector Store Schema
The following collection will be created in Qdrant:

```json
{
  "collection_name": "book_embeddings",
  "vector_size": 384,  // Size for sentence-transformer embeddings
  "distance": "Cosine",
  "hnsw_config": {
    "m": 16,
    "ef_construct": 100
  },
  "optimizers_config": {
    "deleted_threshold": 0.2,
    "vacuum_min_vector_number": 1000
  },
  "payload_schema": {
    "document_chunk_id": {
      "type": "keyword"
    },
    "source_module": {
      "type": "keyword"
    },
    "source_chapter": {
      "type": "keyword"
    },
    "source_section": {
      "type": "keyword"
    },
    "source_url": {
      "type": "text"
    }
  }
}
```

## Relationships

### Entity Relationships
- ChatSession (1) → (Many) ChatQuery: A session can have multiple queries
- ChatQuery (1) → (1) ChatResponse: Each query has one response
- DocumentChunk (1) → (1) VectorEmbedding: Each chunk has one embedding
- ChatResponse (Many) → (Many) DocumentChunk: A response can reference multiple chunks
- DocumentMetadata (1) → (Many) DocumentChunk: A document can be split into multiple chunks

## Data Flow Considerations

### Ingestion Flow
1. Book content is parsed from markdown files
2. Content is split into semantically meaningful chunks
3. Each chunk gets a unique ID and metadata
4. Embeddings are generated for each chunk
5. Chunks and metadata are stored in PostgreSQL
6. Embeddings are stored in Qdrant with payload linking to PostgreSQL records

### Query Flow
1. User query is received with context mode
2. Query is converted to embedding
3. Similarity search is performed in Qdrant
4. Relevant chunks are retrieved based on similarity scores
5. Retrieved chunks are used to construct a prompt for the LLM
6. LLM generates a response based on the context
7. Response is returned to the user with source citations