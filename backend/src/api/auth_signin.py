from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel

from ..database import get_db
from ..models.user import User, UserResponse
from ..utils.password import verify_password
from ..utils.jwt import create_access_token
from ..config.auth import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

router = APIRouter()

class SigninRequest(BaseModel):
    email: str
    password: str

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