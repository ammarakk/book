from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime


class ChatQuery(BaseModel):
    """
    Represents a user's question submitted to the chatbot system
    """
    id: Optional[str] = None
    session_id: Optional[str] = None
    question_text: str
    context_mode: str  # 'global' for full book context or 'selection' for selected text only
    selected_text: Optional[str] = None  # Text that was selected when context_mode is 'selection'
    timestamp: Optional[datetime] = None
    user_id: Optional[str] = None


class ChatResponse(BaseModel):
    """
    The system's answer to a user's query
    """
    id: Optional[str] = None
    query_id: Optional[str] = None
    answer_text: str
    source_chunks: List[str]  # IDs of the document chunks that informed the answer
    confidence_level: float  # Confidence score between 0 and 1
    retrieval_metadata: Optional[Dict[str, Any]] = None
    timestamp: Optional[datetime] = None


class ChatSession(BaseModel):
    """
    A user's interaction session with the chatbot
    """
    id: str
    user_id: Optional[str] = None
    created_at: Optional[datetime] = None
    last_activity_at: Optional[datetime] = None
    is_active: bool = True


class ChatRequest(BaseModel):
    """
    Request model for chat endpoint
    """
    question: str
    session_id: Optional[str] = None


class SelectionChatRequest(BaseModel):
    """
    Request model for chat with selected text context
    """
    question: str
    selected_text: str
    session_id: Optional[str] = None


class ChatHistory(BaseModel):
    """
    Model representing chat history for a session
    """
    session_id: str
    queries_and_responses: List[Dict[str, Any]]