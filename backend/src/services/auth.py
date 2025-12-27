from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import Optional
import uuid
from datetime import datetime

from ..models.user import User, UserCreate
from ..models.profile import Profile, ProfileCreate, BackgroundLevel, HardwareExperience
from ..utils.password import get_password_hash
from ..utils.jwt import create_access_token
from ..config.auth import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

class AuthService:
    @staticmethod
    def register_user(
        db: Session, 
        email: str, 
        password: str,
        software_background: BackgroundLevel,
        hardware_background: HardwareExperience
    ) -> dict:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )
        
        # Hash the password
        hashed_password = get_password_hash(password)
        
        # Create the user
        db_user = User(
            id=str(uuid.uuid4()),
            email=email,
            hashed_password=hashed_password,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        # Create the profile with provided background information
        db_profile = Profile(
            user_id=db_user.id,
            software_background=software_background,
            hardware_background=hardware_background,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        
        # Create access token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": db_user.id}, expires_delta=access_token_expires
        )
        
        # Return user data with token
        return {
            "user_id": db_user.id,
            "email": db_user.email,
            "profile": {
                "software_background": db_profile.software_background,
                "hardware_background": db_profile.hardware_background
            },
            "token": access_token
        }
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[dict]:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None

        # Verify the password
        from ..utils.password import verify_password
        if not verify_password(password, user.hashed_password):
            return None

        # Create access token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.id}, expires_delta=access_token_expires
        )

        return {
            "user_id": user.id,
            "email": user.email,
            "token": access_token
        }