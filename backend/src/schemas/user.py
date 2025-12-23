from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PersonalizationSettingsBase(BaseModel):
    content_depth: Optional[str] = "intermediate"  # 'beginner', 'intermediate', 'advanced'
    preferred_language: Optional[str] = "en"  # 'en', 'ur'
    learning_preferences: Optional[str] = None  # JSON string


class PersonalizationSettingsUpdate(PersonalizationSettingsBase):
    pass


class PersonalizationSettingsResponse(PersonalizationSettingsBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True