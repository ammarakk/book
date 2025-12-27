from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials
from typing import Optional

from ..database import get_db
from ..middleware.auth import JWTBearer

router = APIRouter()
security = JWTBearer()

@router.post("/logout", response_model=dict)
def logout(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    # In a real implementation, you might want to add the token to a blacklist
    # For now, we just return a success message
    return {
        "message": "Successfully logged out"
    }