from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional
import jwt
from datetime import datetime, timedelta
from src.database.database import get_db
from src.models.user import User
from src.schemas.auth import UserCreate, UserLogin, UserResponse
from src.config import settings
from passlib.context import CryptContext

router = APIRouter()
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm="HS256")
    return encoded_jwt


@router.post("/signup", response_model=UserResponse, tags=["auth"])
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user account with background information.
    """
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    
    # Hash the password
    hashed_password = get_password_hash(user_data.password)
    
    # Create new user
    db_user = User(
        email=user_data.email,
        password_hash=hashed_password,
        name=user_data.name,
        software_background=user_data.software_background,
        hardware_background=user_data.hardware_background,
        ai_experience=user_data.ai_experience
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


@router.post("/signin", tags=["auth"])
def signin(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate user and return session token.
    """
    # Find user by email
    user = db.query(User).filter(User.email == user_data.email).first()
    
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # Create access token
    access_token = create_access_token(data={"sub": user.email, "user_id": user.id})
    
    return {
        "token": access_token,
        "user": UserResponse.from_orm(user)
    }


@router.post("/signout", tags=["auth"])
def signout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    End user session.
    """
    # In a real implementation, you might add the token to a blacklist
    return {"message": "Successfully signed out"}