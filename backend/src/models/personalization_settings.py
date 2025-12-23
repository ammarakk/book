from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database.database import Base


class UserPersonalizationSettings(Base):
    __tablename__ = "user_personalization_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    content_depth = Column(String(50), default="intermediate")  # 'beginner', 'intermediate', 'advanced'
    preferred_language = Column(String(10), default="en")  # 'en', 'ur'
    learning_preferences_json = Column(Text)  # JSON data stored as text
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship
    user = relationship("User", back_populates="personalization_settings")

    def __repr__(self):
        return f"<UserPersonalizationSettings(id={self.id}, user_id={self.user_id})>"


