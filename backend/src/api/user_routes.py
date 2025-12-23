from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional
import jwt
from datetime import datetime
from src.database.database import get_db
from src.models.user import User
from src.models.personalization_settings import UserPersonalizationSettings
from src.schemas.user import PersonalizationSettingsResponse, PersonalizationSettingsUpdate
from src.config import settings

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


@router.get("/me/personalization", response_model=PersonalizationSettingsResponse, tags=["users"])
def get_personalization_settings(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Retrieve the current user's personalization settings.
    """
    settings = db.query(UserPersonalizationSettings).filter(
        UserPersonalizationSettings.user_id == current_user.id
    ).first()
    
    if not settings:
        # Create default settings if none exist
        new_settings = UserPersonalizationSettings(
            user_id=current_user.id,
            content_depth="intermediate",
            preferred_language="en"
        )
        db.add(new_settings)
        db.commit()
        db.refresh(new_settings)
        return new_settings
    
    return settings


@router.put("/me/personalization", response_model=PersonalizationSettingsResponse, tags=["users"])
def update_personalization_settings(
    settings_update: PersonalizationSettingsUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update the current user's personalization settings.
    """
    settings = db.query(UserPersonalizationSettings).filter(
        UserPersonalizationSettings.user_id == current_user.id
    ).first()
    
    if not settings:
        # Create new settings if none exist
        settings = UserPersonalizationSettings(user_id=current_user.id)
        db.add(settings)
    
    # Update settings
    settings.content_depth = settings_update.content_depth or settings.content_depth
    settings.preferred_language = settings_update.preferred_language or settings.preferred_language
    settings.learning_preferences = settings_update.learning_preferences or settings.learning_preferences
    
    db.commit()
    db.refresh(settings)
    
    return settings