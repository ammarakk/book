# AI-Driven Physical AI & Humanoid Robotics Book Platform

This project creates an interactive textbook on Physical AI & Humanoid Robotics with integrated AI features, personalization, and translation capabilities.

## Features

- Interactive textbook on Physical AI & Humanoid Robotics
- User authentication and personalization
- AI-powered chatbot with context-aware responses
- Content translation (English ↔ Urdu)
- Neon-themed UI with interactive elements

## Tech Stack

- **Frontend**: Docusaurus, React
- **Backend**: FastAPI, Python
- **Database**: PostgreSQL (Neon Serverless)
- **Vector DB**: Qdrant Cloud
- **AI Services**: Ollama, Cohere
- **Authentication**: BetterAuth

## Setup

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.9 or higher)
- PostgreSQL (or access to Neon Serverless)
- Ollama running locally (for AI services)
- Git

### Environment Setup

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [your-repo-name]
```

2. Create environment files for both frontend and backend:

**Frontend (.env):**
```
REACT_APP_API_BASE_URL=http://localhost:8000
REACT_APP_OLLAMA_URL=http://localhost:11434
```

**Backend (.env):**
```
DATABASE_URL=postgresql://username:password@localhost:5432/book_platform
NEON_DATABASE_URL=your_neon_connection_string
QDRANT_URL=your_qdrant_cloud_url
OLLAMA_URL=http://localhost:11434
JWT_SECRET=your_jwt_secret_key
BETTER_AUTH_SECRET=your_better_auth_secret
```

### Frontend Setup (Docusaurus)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`.

### Backend Setup (FastAPI)

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
uvicorn main:app --reload --port 8000
```

The backend API will be available at `http://localhost:8000`, with documentation at `http://localhost:8000/docs`.

### Setting up Ollama

1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull the required model:
```bash
ollama pull llama3
```
3. Run Ollama:
```bash
ollama serve
```

## API Endpoints

For a complete list of API endpoints, visit `http://localhost:8000/docs` when the backend is running.

## Key Features

### Content Management
- Book content is stored in the `frontend/docs` directory in Markdown format
- Modules and chapters follow the structure defined in the data model
- Content can be personalized based on user preferences

### Authentication
- Users can sign up and sign in using the `/api/auth/signup` and `/api/auth/signin` endpoints
- Authentication state is managed using JWT tokens

### AI Chatbot
- Interact with the AI through the chat interface
- The chatbot uses RAG (Retrieval Augmented Generation) to provide context-aware responses
- Responses are generated using Ollama with the book content as context

### Translation
- Content can be translated from English to Urdu using the translation API
- Translation is triggered via the UI translation button