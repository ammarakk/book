from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials

from ..database import get_db
from ..middleware.auth import JWTBearer, verify_jwt

router = APIRouter()
security = JWTBearer()

@router.get("/protected-example", response_model=dict)
def protected_endpoint(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    # Extract user_id from the token
    token = credentials.credentials
    user_id = verify_jwt(token)
    
    # In a real implementation, you would use the user_id to fetch user-specific data
    # For this example, we'll just return a success message
    return {
        "message": "This is a protected endpoint",
        "user_id": user_id,
        "detail": "Access granted to authenticated user"
    }