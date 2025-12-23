from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database.database import Base


class ContentTranslation(Base):
    __tablename__ = "content_translations"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("book_contents.id"), nullable=False, index=True)
    source_language = Column(String(10), nullable=False)  # 'en'
    target_language = Column(String(10), nullable=False)  # 'ur'
    translated_content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_approved = Column(Boolean, default=False)

    # Relationship
    content = relationship("BookContent", back_populates="translations")

    def __repr__(self):
        return f"<ContentTranslation(id={self.id}, content_id={self.content_id}, target='{self.target_language}')>"


