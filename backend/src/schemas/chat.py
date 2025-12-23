from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class ChatSessionBase(BaseModel):
    title: str


class ChatSessionCreate(ChatSessionBase):
    pass


class ChatSessionUpdate(ChatSessionBase):
    pass


class ChatSessionResponse(ChatSessionBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_active: bool = True
    
    class Config:
        from_attributes = True


class ChatMessageBase(BaseModel):
    content: str
    context: Optional[Dict[str, Any]] = None


class ChatMessageCreate(ChatMessageBase):
    pass


class ChatMessageUpdate(ChatMessageBase):
    pass


class ChatMessageResponse(ChatMessageBase):
    id: int
    chat_session_id: int
    sender_type: str  # 'user' or 'assistant'
    created_at: datetime
    message_number: int
    
    class Config:
        from_attributes = True