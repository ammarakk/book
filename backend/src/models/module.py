from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database.database import Base


class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    module_number = Column(Integer, nullable=False)
    hero_image_url = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_published = Column(Boolean, default=True)
    metadata_json = Column(Text)  # JSON data stored as text

    # Relationship to BookContent
    contents = relationship("BookContent", order_by="BookContent.chapter_number", back_populates="module")

    def __repr__(self):
        return f"<Module(id={self.id}, title='{self.title}', module_number={self.module_number})>"