from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database.database import Base


class UserContentInteraction(Base):
    __tablename__ = "user_content_interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    content_id = Column(Integer, ForeignKey("book_contents.id"), nullable=False, index=True)
    interaction_type = Column(String(50), nullable=False)  # 'view', 'personalize', 'translate', 'bookmark'
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    interaction_data_json = Column(Text)  # JSON data stored as text

    # Relationships
    user = relationship("User", back_populates="content_interactions")
    content = relationship("BookContent", back_populates="user_interactions")

    def __repr__(self):
        return f"<UserContentInteraction(id={self.id}, user_id={self.user_id}, content_id={self.content_id}, type='{self.interaction_type}')>"


