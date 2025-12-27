from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from typing import Optional
import uuid
import jwt
from datetime import datetime

from ..models.translation import (
    TranslationSession,
    TranslationSessionCreate,
    TranslatedContent,
    TranslatedContentCreate
)
from ..services.translation import TranslationService
from ..config.translation import config

router = APIRouter()
security = HTTPBearer()

def verify_jwt_token(token: str) -> str:
    """
    Verify the JWT token and return the user ID
    """
    try:
        # Decode the JWT token using the secret from config
        payload = jwt.decode(
            token,
            config.jwt_secret,
            algorithms=["HS256"]
        )
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/request", response_model=dict)
async def request_translation(
    chapter_id: str,
    target_language: str,
    token: str = Depends(security)
):
    """
    Request translation of a specific chapter from English to the target language
    """
    # Verify the JWT token and extract user ID
    user_id = verify_jwt_token(token.credentials)

    # Validate target language
    if target_language != "ur":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only Urdu (ur) translation is supported"
        )

    # Create a translation session
    session_data = TranslationSessionCreate(
        user_id=user_id,
        chapter_id=chapter_id,
        source_language="en",
        target_language=target_language,
        translation_state="active"
    )

    session = TranslationService.create_session(session_data)

    # Generate translated content using Claude Code Subagents
    translated_contents = TranslationService.generate_translated_content(
        session.session_id,
        chapter_id,
        target_language
    )

    return {
        "session_id": session.session_id,
        "chapter_id": chapter_id,
        "source_language": session.source_language,
        "target_language": session.target_language,
        "translated_content": [content.model_dump() for content in translated_contents],
        "status": "completed"
    }


@router.get("/session/{session_id}", response_model=dict)
async def get_translation_session(
    session_id: str,
    token: str = Depends(security)
):
    """
    Retrieve translated content for an existing translation session
    """
    # Verify the JWT token and extract user ID
    user_id = verify_jwt_token(token.credentials)

    # Verify session belongs to user
    session = TranslationService.get_session(session_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    # Verify that the session belongs to the current user
    if session.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this session"
        )

    contents = TranslationService.get_contents_by_session(session_id)

    return {
        "session_id": session.session_id,
        "chapter_id": session.chapter_id,
        "source_language": session.source_language,
        "target_language": session.target_language,
        "translated_content": [content.model_dump() for content in contents],
        "status": session.translation_state
    }