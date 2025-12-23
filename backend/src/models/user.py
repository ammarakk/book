from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    software_background = Column(String(100))
    hardware_background = Column(String(100))
    ai_experience = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login_at = Column(DateTime(timezone=True))
    is_active = Column(Boolean, default=True)
    preferences_json = Column(Text)  # JSON data stored as text

    # Relationships
    personalization_settings = relationship("UserPersonalizationSettings", back_populates="user")
    content_interactions = relationship("UserContentInteraction", back_populates="user")
    chat_sessions = relationship("ChatSession", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', name='{self.name}')>"