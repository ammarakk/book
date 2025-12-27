from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from typing import Dict, Any, Optional
import uuid
from datetime import datetime

from models.chat import ChatRequest, SelectionChatRequest, ChatResponse as ChatResponseModel
from models.database import ChatQuery, ChatResponse as DBChatResponse, ChatSession
from services.rag_service import RagService
from services.document_service import DocumentService
from services.embedding_service import EmbeddingService
from config import settings


router = APIRouter()


@router.post("/chat", response_model=ChatResponseModel)
async def chat_endpoint(chat_request: ChatRequest):
    """
    Endpoint to handle general chat queries about the book content
    """
    # Initialize services
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import sessionmaker

    # This is a simplified implementation - in practice, you'd want to inject these dependencies
    # properly using FastAPI's dependency system
    engine = create_async_engine(settings.NEON_DATABASE_URL)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        document_service = DocumentService(session)
        embedding_service = EmbeddingService()
        rag_service = RagService(document_service, embedding_service)

        # Create a chat query object
        query_obj = ChatQuery(
            id=str(uuid.uuid4()),
            session_id=chat_request.session_id or f"session-{int(datetime.utcnow().timestamp())}",
            question_text=chat_request.question,
            context_mode="global",  # Default to global context
            selected_text=None,
            timestamp=datetime.utcnow(),
            user_id=None  # Would come from auth if implemented later
        )

        # Process the query through the RAG pipeline
        response = await rag_service.process_query(query_obj)

        # Save the query and response to the database
        # In a real implementation, this would be done with proper SQLAlchemy ORM operations

        return ChatResponseModel(
            id=response.id,
            query_id=response.query_id,
            answer_text=response.answer_text,
            source_chunks=response.source_chunks,
            confidence_level=response.confidence_level,
            retrieval_metadata=response.retrieval_metadata,
            timestamp=response.timestamp
        )


@router.post("/chat/selection", response_model=ChatResponseModel)
async def chat_selection_endpoint(selection_request: SelectionChatRequest):
    """
    Endpoint to handle chat queries with selected text context only
    """
    # Initialize services
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import sessionmaker

    # This is a simplified implementation - in practice, you'd want to inject these dependencies
    # properly using FastAPI's dependency system
    engine = create_async_engine(settings.NEON_DATABASE_URL)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        document_service = DocumentService(session)
        embedding_service = EmbeddingService()
        rag_service = RagService(document_service, embedding_service)

        # Create a chat query object with selection context
        query_obj = ChatQuery(
            id=str(uuid.uuid4()),
            session_id=selection_request.session_id or f"session-{int(datetime.utcnow().timestamp())}",
            question_text=selection_request.question,
            context_mode="selection",  # Specific to selected text
            selected_text=selection_request.selected_text,
            timestamp=datetime.utcnow(),
            user_id=None  # Would come from auth if implemented later
        )

        # Process the query through the RAG pipeline
        response = await rag_service.process_query(query_obj)

        # Save the query and response to the database
        # In a real implementation, this would be done with proper SQLAlchemy ORM operations

        return ChatResponseModel(
            id=response.id,
            query_id=response.query_id,
            answer_text=response.answer_text,
            source_chunks=response.source_chunks,
            confidence_level=response.confidence_level,
            retrieval_metadata=response.retrieval_metadata,
            timestamp=response.timestamp
        )


@router.get("/chat/history/{session_id}")
async def get_chat_history(session_id: str):
    """
    Retrieve the chat history for a specific session
    """
    # In a real implementation, this would query the database for chat history
    # For now, returning an empty list as a placeholder
    return {"session_id": session_id, "history": []}


@router.delete("/chat/session/{session_id}")
async def clear_chat_session(session_id: str):
    """
    Clear the chat history for a specific session
    """
    # In a real implementation, this would delete the chat history from the database
    # For now, returning a success message as a placeholder
    return {"session_id": session_id, "message": "Session cleared successfully"}