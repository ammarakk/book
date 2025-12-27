from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import Optional
from datetime import datetime

from ..models.profile import Profile, ProfileCreate, ProfileUpdate, ProfileResponse, BackgroundLevel, HardwareExperience

class ProfileService:
    @staticmethod
    def create_profile(
        db: Session,
        user_id: str,
        software_background: BackgroundLevel,
        hardware_background: HardwareExperience
    ) -> ProfileResponse:
        # Check if profile already exists for this user
        existing_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if existing_profile:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Profile already exists for this user"
            )
        
        # Create the profile
        db_profile = Profile(
            user_id=user_id,
            software_background=software_background,
            hardware_background=hardware_background,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        
        return ProfileResponse(
            user_id=db_profile.user_id,
            software_background=db_profile.software_background,
            hardware_background=db_profile.hardware_background,
            created_at=db_profile.created_at,
            updated_at=db_profile.updated_at
        )
    
    @staticmethod
    def get_profile(db: Session, user_id: str) -> Optional[ProfileResponse]:
        db_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if not db_profile:
            return None
        
        return ProfileResponse(
            user_id=db_profile.user_id,
            software_background=db_profile.software_background,
            hardware_background=db_profile.hardware_background,
            created_at=db_profile.created_at,
            updated_at=db_profile.updated_at
        )
    
    @staticmethod
    def update_profile(
        db: Session,
        user_id: str,
        profile_update: ProfileUpdate
    ) -> Optional[ProfileResponse]:
        db_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if not db_profile:
            return None
        
        # Update fields if provided
        if profile_update.software_background is not None:
            db_profile.software_background = profile_update.software_background
        if profile_update.hardware_background is not None:
            db_profile.hardware_background = profile_update.hardware_background
            
        db_profile.updated_at = datetime.now()
        db.commit()
        db.refresh(db_profile)
        
        return ProfileResponse(
            user_id=db_profile.user_id,
            software_background=db_profile.software_background,
            hardware_background=db_profile.hardware_background,
            created_at=db_profile.created_at,
            updated_at=db_profile.updated_at
        )