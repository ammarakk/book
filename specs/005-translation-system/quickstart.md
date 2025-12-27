# Quickstart: Translation System (English ↔ Urdu)

## Prerequisites

- Node.js 18+ (for Docusaurus frontend)
- Python 3.11+ (for backend services)
- Claude Code API access
- Phase 3 (Authentication) and Phase 4 (Personalization) completed and deployed
- Neon Serverless PostgreSQL database

## Environment Setup

1. **Database Setup**:
   ```bash
   # Ensure your Neon Serverless PostgreSQL database is configured
   # Get your database connection string from Neon dashboard
   ```

2. **Environment Variables**:
   ```bash
   # backend/.env
   CLAUDE_API_KEY="your-claude-api-key"
   JWT_SECRET="your-jwt-secret-key"
   DATABASE_URL="your-neon-db-connection-string"
   ```

## Backend Setup

1. **Install Dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Start Backend**:
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
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
   # Ensure Claude Code Subagents are properly configured with appropriate prompts
   # Configure agent skills for content preservation
   ```

## API Endpoints

- **Request Translation**: `POST http://localhost:8000/api/auth/translate/request`
- **Get Translation Session**: `GET http://localhost:8000/api/auth/translate/session/{session_id}`

## Testing Translation Flow

1. **Log in** to the application with an authenticated account

2. **Navigate to a chapter** in the book

3. **Click the "Translate to Urdu" button** to request Urdu translation

4. **View the translated content** that appears with visual distinction from original content

5. **Verify that code blocks remain in English** while text is translated to Urdu

6. **Test the logout functionality** to ensure translation access is properly restricted

## Frontend Integration

The translation feature is integrated into the Docusaurus documentation pages:

```javascript
// Example integration in a documentation page
import { TranslationToggle } from './components/TranslationToggle';
import { TranslatedContent } from './components/TranslatedContent';

function DocPage() {
  return (
    <div>
      <header>
        <h1>Chapter Title</h1>
        <TranslationToggle chapterId="current-chapter-id" />
      </header>

      <main>
        {/* Original book content */}
        <div className="original-content">
          {/* The original English chapter content */}
        </div>

        {/* Translated content will appear here when activated */}
        <TranslatedContent chapterId="current-chapter-id" />
      </main>
    </div>
  );
}
```

## Agent Skills Usage

The translation system uses Claude Code Subagents with specialized skills:

- **TechnicalTermPreservation**: Ensures technical terms remain unchanged during translation
- **CodeBlockProtection**: Identifies and protects code blocks from translation
- **FormattingMaintenance**: Preserves document structure and formatting during translation