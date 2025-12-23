from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from src.schemas.translation import TranslationRequest, TranslationResponse
from src.services.translation_service import TranslationService

router = APIRouter()


@router.post("/", response_model=TranslationResponse, tags=["translation"])
def translate_content(translation_request: TranslationRequest):
    """
    Translate content from one language to another.
    """
    try:
        # Use translation service to translate content
        translation_service = TranslationService()
        translated_content = translation_service.translate(
            translation_request.content,
            translation_request.source_language,
            translation_request.target_language
        )
        
        return TranslationResponse(
            translated_content=translated_content,
            source_language=translation_request.source_language,
            target_language=translation_request.target_language
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")