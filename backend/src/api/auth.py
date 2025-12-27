from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
import uuid
from datetime import datetime
from pydantic import BaseModel
from fastapi.security import HTTPAuthorizationCredentials

from ..database import get_db
from ..models.user import User, UserCreate, UserResponse
from ..models.profile import Profile, ProfileCreate, BackgroundLevel, HardwareExperience
from ..utils.password import get_password_hash, verify_password
from ..utils.jwt import create_access_token
from ..config.auth import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from ..middleware.auth import JWTBearer

security = JWTBearer()
router = APIRouter()

class SignupRequest(UserCreate):
    software_background: BackgroundLevel
    hardware_background: HardwareExperience

class SigninRequest(BaseModel):
    email: str
    password: str

@router.post("/signup", response_model=dict)
def signup(request_data: SignupRequest, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == request_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Hash the password
    hashed_password = get_password_hash(request_data.password)

    # Create the user
    db_user = User(
        id=str(uuid.uuid4()),
        email=request_data.email,
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
        software_background=request_data.software_background,
        hardware_background=request_data.hardware_background,
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

@router.post("/signin", response_model=dict)
def signin(request_data: SigninRequest, db: Session = Depends(get_db)):
    # Find user by email
    user = db.query(User).filter(User.email == request_data.email).first()

    # Check if user exists and password is correct
    if not user or not verify_password(request_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )

    # Return user data with token
    return {
        "user_id": user.id,
        "email": user.email,
        "token": access_token
    }


@router.post("/logout", response_model=dict)
def logout(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    # In a real implementation, you might want to add the token to a blacklist
    # For now, we just return a success message
    return {
        "message": "Successfully logged out"
    }