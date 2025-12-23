# Import all schemas to make them available when importing the schemas package
from .content import ModuleResponse, BookContentResponse
from .auth import UserCreate, UserLogin, UserResponse
from .user import PersonalizationSettingsResponse, PersonalizationSettingsUpdate
from .chat import ChatSessionResponse, ChatMessageResponse
from .translation import TranslationRequest, TranslationResponse

__all__ = [
    "ModuleResponse",
    "BookContentResponse",
    "UserCreate",
    "UserLogin",
    "UserResponse",
    "PersonalizationSettingsResponse",
    "PersonalizationSettingsUpdate",
    "ChatSessionResponse",
    "ChatMessageResponse",
    "TranslationRequest",
    "TranslationResponse",
]