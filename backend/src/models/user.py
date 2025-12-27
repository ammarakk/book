from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import uuid

class User(BaseModel):
    id: str = str(uuid.uuid4())
    email: EmailStr
    hashed_password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class UserCreate(BaseModel):
    email: EmailStr
    password: str  # Plain text password that will be hashed

class UserResponse(BaseModel):
    id: str
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True