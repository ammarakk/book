from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database.database import Base


class BookContent(Base):
    __tablename__ = "book_contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False, index=True)
    content = Column(Text, nullable=False)  # Markdown content
    content_urdu = Column(Text)  # Urdu translation of content
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    chapter_number = Column(Integer, nullable=False)
    type = Column(String(50), nullable=False)  # 'module', 'chapter', 'section'
    parent_id = Column(Integer, ForeignKey("book_contents.id"))  # Self-referencing
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_published = Column(Boolean, default=True)
    metadata_json = Column(Text)  # JSON data stored as text

    # Relationships
    module = relationship("Module", back_populates="contents")
    parent = relationship("BookContent", remote_side=[id], back_populates="children")
    children = relationship("BookContent", back_populates="parent", overlaps="parent")
    user_interactions = relationship("UserContentInteraction", back_populates="content")
    translations = relationship("ContentTranslation", back_populates="content")

    def __repr__(self):
        return f"<BookContent(id={self.id}, title='{self.title}', type='{self.type}')>"