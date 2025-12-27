from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

class BackgroundLevel(str):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class HardwareExperience(str):
    NONE = "none"
    BASIC_ELECTRONICS = "basic_electronics"
    ROBOTICS_EXPERIENCE = "robotics_experience"

class Profile(BaseModel):
    user_id: str
    software_background: BackgroundLevel
    hardware_background: HardwareExperience
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class ProfileCreate(BaseModel):
    software_background: BackgroundLevel
    hardware_background: HardwareExperience

class ProfileUpdate(BaseModel):
    software_background: Optional[BackgroundLevel] = None
    hardware_background: Optional[HardwareExperience] = None

class ProfileResponse(BaseModel):
    user_id: str
    software_background: BackgroundLevel
    hardware_background: HardwareExperience
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True