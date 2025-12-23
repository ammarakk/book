from sqlalchemy.orm import Session
from typing import Dict, Any, Optional
from src.services.ollama_service import OllamaService
from src.services.rag_service import RagService


class ChatService:
    """
    Service to handle chat interactions and AI responses.
    """
    
    def __init__(self, db: Session):
        self.db = db
        self.ollama_service = OllamaService()
        self.rag_service = RagService(db)
    
    def generate_response(self, user_message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a response to the user's message using AI.
        """
        # If context is provided (e.g., selected text), use RAG to get relevant information
        context_text = ""
        if context:
            # Extract relevant information based on context
            if "selected_text" in context:
                # Use RAG to find related content
                context_text = self.rag_service.get_relevant_content(context["selected_text"])
            elif "chapter_id" in context:
                # Get content from the specified chapter
                context_text = self.rag_service.get_content_by_chapter(context["chapter_id"])
        
        # Generate response using Ollama with the context
        response = self.ollama_service.generate_response(user_message, context_text)
        
        return response