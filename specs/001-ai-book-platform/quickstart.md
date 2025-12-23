# Quickstart Guide: AI-Driven Physical AI & Humanoid Robotics Book Platform

## Development Setup

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
```env
REACT_APP_API_BASE_URL=http://localhost:8000
REACT_APP_OLLAMA_URL=http://localhost:11434
```

**Backend (.env):**
```env
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

### Database Setup

1. If using local PostgreSQL:
   - Create a database named `book_platform`
   - Update the DATABASE_URL in your backend .env file

2. If using Neon:
   - Create a Neon project
   - Update the NEON_DATABASE_URL in your backend .env file
   - Run migrations (see below)

3. Run database migrations:
```bash
cd backend
python -m alembic upgrade head
```

## Running the Application

### Development Mode

1. Start Ollama (in a separate terminal):
```bash
ollama serve
```

2. Start the backend (in a separate terminal):
```bash
cd backend
uvicorn main:app --reload --port 8000
```

3. Start the frontend (in a separate terminal):
```bash
cd frontend
npm start
```

### Production Build

1. Build the frontend:
```bash
cd frontend
npm run build
```

2. The built files will be in the `build` directory and can be served statically.

## Key Features

### Content Management
- Book content is stored in the `frontend/docs` directory in Markdown format
- Modules and chapters follow the structure defined in `data-model.md`
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

## API Endpoints

For a complete list of API endpoints, visit `http://localhost:8000/docs` when the backend is running.

## Troubleshooting

### Common Issues

1. **Port already in use**: Make sure no other processes are using ports 3000 (frontend) or 8000 (backend)

2. **Database connection errors**: Verify your PostgreSQL/Neon connection string is correct in the .env file

3. **Ollama not responding**: Ensure Ollama is running and the model is downloaded

4. **Frontend can't connect to backend**: Check that the API_BASE_URL in frontend .env matches your backend URL

### Verifying Setup

1. Visit `http://localhost:3000` - you should see the book platform
2. Visit `http://localhost:8000/docs` - you should see the API documentation
3. Verify Ollama is running by visiting `http://localhost:11434/api/tags` - you should see your available models