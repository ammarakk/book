import os
from typing import Optional
from pydantic import field_validator
from pydantic_settings import BaseSettings


class PersonalizationConfig(BaseSettings):
    """
    Configuration for the personalization service
    """
    claude_api_key: str = os.getenv("CLAUDE_API_KEY", "")
    claude_api_base_url: str = os.getenv("CLAUDE_API_BASE_URL", "https://api.anthropic.com/v1/messages")
    claude_api_version: str = os.getenv("CLAUDE_API_VERSION", "2023-06-01")
    claude_default_model: str = os.getenv("CLAUDE_DEFAULT_MODEL", "claude-3-opus-20240229")

    jwt_secret: str = os.getenv("JWT_SECRET", "")
    database_url: str = os.getenv("DATABASE_URL", "")

    # Personalization settings
    max_tokens_for_completion: int = int(os.getenv("MAX_TOKENS_FOR_COMPLETION", "1000"))
    timeout_for_api_call: int = int(os.getenv("TIMEOUT_FOR_API_CALL", "30"))

    class Config:
        env_file = ".env"
        case_sensitive = True

    @field_validator('claude_api_key')
    @classmethod
    def claude_api_key_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('CLAUDE_API_KEY must be set in environment variables')
        return v

    @field_validator('jwt_secret')
    @classmethod
    def jwt_secret_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('JWT_SECRET must be set in environment variables')
        return v


# Global configuration instance
config = PersonalizationConfig()


def get_config() -> PersonalizationConfig:
    """
    Get the configuration instance
    """
    return config