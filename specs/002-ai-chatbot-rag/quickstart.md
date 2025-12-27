# Quickstart Guide: AI Chatbot (RAG System) for Physical AI & Humanoid Robotics Book

## Overview
This guide will help you set up and run the AI Chatbot (RAG System) for the Physical AI & Humanoid Robotics book locally.

## Prerequisites
- Python 3.11+ installed
- Node.js v20+ installed
- Ollama installed and running with a supported model (e.g., llama3)
- Access to Qdrant Cloud (Free Tier)
- Access to Neon Serverless PostgreSQL
- Git

## Setup Instructions

### Backend Setup (RAG System)

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your actual configuration
```

5. Run the backend service:
```bash
uvicorn main:app --reload
```

### Frontend Setup (Docusaurus Book with Chatbot)

1. Navigate to the Docusaurus project:
```bash
cd docusaurus/physical-ai-book
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run start
```

4. Open your browser to [http://localhost:3000](http://localhost:3000) to view the book with the embedded chatbot.

## Configuration

### Environment Variables
The backend requires the following environment variables:

- `OLLAMA_MODEL`: The Ollama model to use (e.g., llama3, mistral)
- `OLLAMA_BASE_URL`: Base URL for the Ollama service
- `QDRANT_URL`: URL for the Qdrant Cloud instance
- `QDRANT_API_KEY`: API key for Qdrant Cloud
- `NEON_DATABASE_URL`: Connection string for Neon Serverless PostgreSQL

### API Endpoints
The backend provides the following API endpoints:

- `POST /chat`: Submit a question to the chatbot
- `POST /chat/selection`: Submit a question with selected text context
- `GET /health`: Health check for the service

## Running Tests

### Backend Tests
```bash
cd backend
python -m pytest tests/
```

### Frontend Tests
```bash
cd docusaurus/physical-ai-book
npm test
```

## Building for Production

### Backend
The backend is a FastAPI application that can be deployed using any ASGI server like uvicorn or gunicorn.

### Frontend
To build the Docusaurus site for production:
```bash
npm run build
```

The built site will be in the `build/` directory and can be served by any static hosting service.

## Troubleshooting

### Common Issues

1. **Ollama Connection Error**: Ensure Ollama is running and the model is pulled:
   ```bash
   ollama serve  # Start Ollama server
   ollama pull llama3  # Pull the required model
   ```

2. **Qdrant Connection Error**: Verify the URL and API key in your environment variables.

3. **Neon Database Connection Error**: Check the database URL and ensure the schema is properly set up.

### Verifying the Setup
1. Check that the backend is running: `curl http://localhost:8000/health`
2. Verify the frontend is accessible: Open the site in your browser
3. Test the chat functionality by asking a question about the book content