from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials

from ..database import get_db
from ..models.profile import ProfileResponse, ProfileUpdate
from ..services.profile import ProfileService
from ..middleware.auth import JWTBearer, verify_jwt
from ..models.user import User

router = APIRouter()
security = JWTBearer()

@router.get("/profile", response_model=dict)
def get_profile(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    # Extract user_id from the token
    token = credentials.credentials
    user_id = verify_jwt(token)

    profile = ProfileService.get_profile(db, user_id)

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )

    # Get user email from the user table
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "user_id": profile.user_id,
        "email": user.email,
        "profile": {
            "software_background": profile.software_background,
            "hardware_background": profile.hardware_background
        }
    }

@router.put("/profile", response_model=dict)
def update_profile(
    profile_update: ProfileUpdate,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    # Extract user_id from the token
    token = credentials.credentials
    user_id = verify_jwt(token)

    updated_profile = ProfileService.update_profile(db, user_id, profile_update)

    if not updated_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )

    return {
        "user_id": updated_profile.user_id,
        "profile": {
            "software_background": updated_profile.software_background,
            "hardware_background": updated_profile.hardware_background
        }
    }