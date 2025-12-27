from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from typing import Optional, List
import uuid

Base = declarative_base()


class DocumentMetadata(Base):
    """
    Information about book content stored in the database
    """
    __tablename__ = "document_metadata"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id = Column(String, unique=True, nullable=False)
    source_file_path = Column(Text, nullable=False)
    module_name = Column(String(255), nullable=False)
    chapter_name = Column(String(255), nullable=False)
    section_name = Column(String(255))
    content_hash = Column(String(64), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class ChatSession(Base):
    """
    A user's interaction session with the chatbot
    """
    __tablename__ = "chat_sessions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_activity_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)


class ChatQuery(Base):
    """
    Represents a user's question submitted to the chatbot system
    """
    __tablename__ = "chat_queries"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String, ForeignKey("chat_sessions.id"))
    question_text = Column(Text, nullable=False)
    context_mode = Column(String(20))  # 'global' or 'selection'
    selected_text = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    session = relationship("ChatSession", back_populates="queries")


# Establish the reverse relationship
ChatSession.queries = relationship("ChatQuery", order_by=ChatQuery.timestamp, back_populates="session")


class ChatResponse(Base):
    """
    The system's answer to a user's query
    """
    __tablename__ = "chat_responses"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    query_id = Column(String, ForeignKey("chat_queries.id"))
    answer_text = Column(Text, nullable=False)
    source_chunks = Column(String)  # JSON string of array of document chunk IDs
    confidence_level = Column(Integer)  # Value between 0 and 100
    retrieval_metadata = Column(String)  # JSON string of metadata
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    query = relationship("ChatQuery", back_populates="response")


# Establish the reverse relationship
ChatQuery.response = relationship("ChatResponse", uselist=False, back_populates="query")