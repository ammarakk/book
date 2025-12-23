from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database.database import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_session_id = Column(Integer, ForeignKey("chat_sessions.id"), nullable=False)
    sender_type = Column(String(20), nullable=False)  # 'user', 'assistant'
    content = Column(Text, nullable=False)
    context = Column(Text)  # JSON data stored as text
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    message_number = Column(Integer, nullable=False)

    # Relationship
    session = relationship("ChatSession", back_populates="messages")

    def __repr__(self):
        return f"<ChatMessage(id={self.id}, session_id={self.chat_session_id}, sender='{self.sender_type}')>"