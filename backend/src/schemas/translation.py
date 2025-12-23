from pydantic import BaseModel
from typing import Optional


class TranslationRequest(BaseModel):
    content: str
    source_language: str = "en"
    target_language: str = "ur"


class TranslationResponse(BaseModel):
    translated_content: str
    source_language: str
    target_language: str