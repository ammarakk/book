# Quickstart: AI-Powered Content Personalization

## Prerequisites

- Node.js 18+ (for Docusaurus frontend)
- Python 3.11+ (for backend services)
- Claude Code API access
- Phase 3 (Authentication) completed and deployed
- Neon Serverless PostgreSQL database

## Environment Setup

1. **Database Setup**:
   ```bash
   # Ensure your Neon Serverless PostgreSQL database is configured
   # Update your DATABASE_URL in environment variables
   ```

2. **Environment Variables**:
   ```bash
   # backend/.env
   DATABASE_URL="your-neon-db-connection-string"
   CLAUDE_API_KEY="your-claude-api-key"
   JWT_SECRET="your-jwt-secret-key"
   ```

## Backend Setup

1. **Install Dependencies**:
   ```bash
   cd backend
   pip install fastapi uvicorn python-jose[cryptography] psycopg2-binary
   ```

2. **Start Backend**:
   ```bash
   cd backend
   uvicorn src.main:app --reload --port 8000
   ```

## Frontend Setup

1. **Install Dependencies**:
   ```bash
   cd docusaurus
   npm install
   ```

2. **Start Frontend**:
   ```bash
   cd docusaurus
   npm start
   ```

## Claude Code Subagent Setup

1. **Agent Configuration**:
   ```bash
   # Set up Claude Code Subagents with appropriate prompts
   # Configure agent skills for personalization
   ```

## API Endpoints

- **Request Personalization**: `POST http://localhost:8000/api/personalize/request`
- **Get Session**: `GET http://localhost:8000/api/personalize/session/{session_id}`

## Testing Personalization Flow

1. **Ensure you're logged in** to the application (Phase 3 authentication required)

2. **Navigate to a chapter** in the book

3. **Click the "Personalize Content" button** to request personalized content

4. **View the personalized content** that appears with visual distinction from original content

## Frontend Integration

The personalization feature is integrated into the Docusaurus documentation pages:

```javascript
// Example integration in a documentation page
import { PersonalizeButton } from './components/PersonalizeButton';
import { PersonalizedContent } from './components/PersonalizedContent';

function DocPage() {
  return (
    <div>
      <header>
        <h1>Chapter Title</h1>
        <PersonalizeButton chapterId="current-chapter-id" />
      </header>
      
      <main>
        {/* Original book content */}
        <div className="original-content">
          {/* The original chapter content */}
        </div>
        
        {/* Personalized content will appear here when activated */}
        <PersonalizedContent chapterId="current-chapter-id" />
      </main>
    </div>
  );
}
```

## Agent Skills Usage

The personalization engine uses Claude Code Subagents with specialized skills:

- **Content Simplification**: For beginner-level users
- **Technical Elaboration**: For advanced-level users
- **Terminology Validation**: To ensure technical terms remain unchanged