from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database.database import get_db
from src.models.module import Module
from src.models.book_content import BookContent
from src.schemas.content import ModuleResponse, BookContentResponse

router = APIRouter()


@router.get("/modules", response_model=List[ModuleResponse], tags=["content"])
def get_modules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of available modules.
    """
    modules = db.query(Module).offset(skip).limit(limit).all()
    return modules


@router.get("/modules/{module_id}/chapters", response_model=List[BookContentResponse], tags=["content"])
def get_chapters_for_module(module_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve chapters for a specific module.
    """
    chapters = db.query(BookContent).filter(
        BookContent.module_id == module_id,
        BookContent.type == "chapter"
    ).offset(skip).limit(limit).all()
    
    if not chapters:
        raise HTTPException(status_code=404, detail="No chapters found for this module")
    
    return chapters


@router.get("/chapters/{chapter_id}", response_model=BookContentResponse, tags=["content"])
def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    """
    Retrieve content of a specific chapter.
    """
    chapter = db.query(BookContent).filter(
        BookContent.id == chapter_id,
        BookContent.type == "chapter"
    ).first()
    
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    
    return chapter