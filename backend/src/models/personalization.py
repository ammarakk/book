from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime
import uuid


class PersonalizationSessionBase(BaseModel):
    user_id: str
    chapter_id: str
    user_profile: Dict[str, str]  # Contains software_background and hardware_background
    personalization_state: str = "inactive"  # "active" or "inactive"


class PersonalizationSessionCreate(PersonalizationSessionBase):
    pass


class PersonalizationSessionUpdate(BaseModel):
    personalization_state: Optional[str] = None


class PersonalizationSession(PersonalizationSessionBase):
    session_id: str = str(uuid.uuid4())
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        from_attributes = True


class PersonalizedContentBase(BaseModel):
    session_id: str
    original_content_id: str
    personalized_text: str
    personalization_type: str  # "explanation", "example", "difficulty-adjustment"
    user_background_level: str  # "beginner", "intermediate", "advanced"


class PersonalizedContentCreate(PersonalizedContentBase):
    pass


class PersonalizedContentUpdate(BaseModel):
    personalized_text: Optional[str] = None


class PersonalizedContent(PersonalizedContentBase):
    content_id: str = str(uuid.uuid4())
    created_at: datetime = datetime.now()

    class Config:
        from_attributes = True