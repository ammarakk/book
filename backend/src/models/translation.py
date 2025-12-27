from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class TranslationSession(Base):
    __tablename__ = "translation_sessions"

    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)  # Foreign key to User.id from Phase 3
    chapter_id = Column(String, nullable=False)
    source_language = Column(String, nullable=False, default="en")
    target_language = Column(String, nullable=False, default="ur")
    translation_state = Column(String, nullable=False, default="inactive")  # "active" or "inactive"
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<TranslationSession(session_id={self.session_id}, user_id={self.user_id}, chapter_id={self.chapter_id})>"


class TranslatedContent(Base):
    __tablename__ = "translated_content"

    content_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), nullable=False)  # Foreign key to TranslationSession.session_id
    original_content_id = Column(String, nullable=False)
    original_text = Column(Text, nullable=False)
    translated_text = Column(Text, nullable=False)
    content_type = Column(String, nullable=False)  # "text", "heading", "code_block", "list_item", "table_cell"
    preservation_flags = Column(String, nullable=True)  # JSON string for preservation flags
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<TranslatedContent(content_id={self.content_id}, session_id={self.session_id})>"