from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List, Optional
import jwt
from datetime import datetime
from src.database.database import get_db
from src.models.user import User
from src.models.chat_session import ChatSession
from src.models.chat_message import ChatMessage
from src.schemas.chat import ChatSessionCreate, ChatSessionResponse, ChatMessageCreate, ChatMessageResponse
from src.config import settings
from src.services.chat_service import ChatService

router = APIRouter()
security = HTTPBearer()


def get_current_user(token: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    """
    Get the current user based on the provided JWT token.
    """
    try:
        payload = jwt.decode(token.credentials, settings.JWT_SECRET, algorithms=["HS256"])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user


@router.post("/", response_model=ChatSessionResponse, tags=["chat"])
def create_chat_session(
    session_data: ChatSessionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new chat session.
    """
    db_session = ChatSession(
        user_id=current_user.id,
        title=session_data.title
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    
    return db_session


@router.post("/{session_id}/messages", response_model=ChatMessageResponse, tags=["chat"])
def send_message(
    session_id: int,
    message_data: ChatMessageCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Send a message to the chatbot and receive a response.
    """
    # Verify that the session belongs to the current user
    session = db.query(ChatSession).filter(
        ChatSession.id == session_id,
        ChatSession.user_id == current_user.id
    ).first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat session not found or access denied"
        )
    
    # Create user message
    user_message = ChatMessage(
        chat_session_id=session_id,
        sender_type="user",
        content=message_data.content,
        context=message_data.context,
        message_number=1  # This would need to be calculated based on existing messages
    )
    db.add(user_message)
    db.commit()
    db.refresh(user_message)
    
    # Generate AI response using chat service
    chat_service = ChatService(db)
    ai_response = chat_service.generate_response(message_data.content, message_data.context)
    
    # Create AI message
    ai_message = ChatMessage(
        chat_session_id=session_id,
        sender_type="assistant",
        content=ai_response,
        message_number=2  # This would need to be calculated based on existing messages
    )
    db.add(ai_message)
    db.commit()
    db.refresh(ai_message)
    
    return ai_message


@router.get("/", response_model=List[ChatSessionResponse], tags=["chat"])
def get_user_chat_sessions(
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve the current user's chat sessions.
    """
    sessions = db.query(ChatSession).filter(
        ChatSession.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    
    return sessions


@router.get("/{session_id}/messages", response_model=List[ChatMessageResponse], tags=["chat"])
def get_chat_messages(
    session_id: int,
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve messages in a specific chat session.
    """
    # Verify that the session belongs to the current user
    session = db.query(ChatSession).filter(
        ChatSession.id == session_id,
        ChatSession.user_id == current_user.id
    ).first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat session not found or access denied"
        )
    
    messages = db.query(ChatMessage).filter(
        ChatMessage.chat_session_id == session_id
    ).order_by(ChatMessage.message_number).offset(skip).limit(limit).all()
    
    return messages