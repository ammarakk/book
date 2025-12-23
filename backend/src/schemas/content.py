from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ModuleBase(BaseModel):
    title: str
    description: Optional[str] = None
    module_number: int
    hero_image_url: Optional[str] = None
    is_published: Optional[bool] = True


class ModuleCreate(ModuleBase):
    pass


class ModuleUpdate(ModuleBase):
    pass


class ModuleResponse(ModuleBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class BookContentBase(BaseModel):
    title: str
    content: str
    content_urdu: Optional[str] = None
    module_id: int
    chapter_number: int
    type: str  # 'module', 'chapter', 'section'
    parent_id: Optional[int] = None
    is_published: Optional[bool] = True


class BookContentCreate(BookContentBase):
    pass


class BookContentUpdate(BookContentBase):
    pass


class BookContentResponse(BookContentBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True