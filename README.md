# Physical AI & Humanoid Robotics Book

Welcome to the Physical AI & Humanoid Robotics Book project! This interactive book aims to teach the fundamentals of physical AI and humanoid robotics through a progressive curriculum.

## Project Structure

This project is organized into multiple phases:

- **Phase 1**: Book Foundation - Core content and structure
- **Phase 2**: AI Chatbot (RAG) - Interactive Q&A system
- **Phase 3**: Authentication & User Profiles - User accounts and authentication
- **Phase 4**: AI-Powered Content Personalization - Personalized learning experiences
- **Phase 5**: Translation System (English ↔ Urdu) - Bilingual content translation

## Technologies Used

- **Frontend**: Docusaurus, React, JavaScript/TypeScript
- **Backend**: FastAPI, Python
- **Database**: Neon Serverless PostgreSQL
- **AI/ML**: Claude Code Subagents for content personalization and translation
- **Authentication**: JWT-based authentication system

## Features

### Authentication & User Profiles
- Secure user registration and login
- Profile management with background information
- JWT-based session management

### AI-Powered Content Personalization
- Adaptive content based on user's software and hardware background
- Claude Code Subagents for generating personalized explanations
- Visual distinction between original and personalized content

### Translation System (English ↔ Urdu)
- User-triggered translation between English and Urdu
- Preserves technical terminology and code blocks
- Available only to authenticated users

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/ammarakk/book.git
   ```

2. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Install frontend dependencies:
   ```bash
   cd docusaurus
   npm install
   ```

4. Set up environment variables (copy `.env.example` to `.env` and update values)

5. Start the backend server:
   ```bash
   cd backend
   python -m uvicorn main:app --reload --port 8000
   ```

6. Start the frontend:
   ```bash
   cd docusaurus
   npm start
   ```

## Contributing

We welcome contributions to improve the book content, add new features, or fix issues. Please follow the project's constitution and phase-based development approach.

## License

This project is licensed under the MIT License - see the LICENSE file for details.