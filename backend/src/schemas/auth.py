from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: str
    name: str
    software_background: Optional[str] = None
    hardware_background: Optional[str] = None
    ai_experience: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    software_background: Optional[str] = None
    hardware_background: Optional[str] = None
    ai_experience: Optional[str] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None
    is_active: bool = True
    
    class Config:
        from_attributes = True