from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    NEON_DATABASE_URL: str = os.getenv("NEON_DATABASE_URL", "")
    
    # Qdrant
    QDRANT_URL: str = os.getenv("QDRANT_URL", "")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
    
    # Ollama
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    
    # Auth
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your-default-secret-change-in-production")
    BETTER_AUTH_SECRET: str = os.getenv("BETTER_AUTH_SECRET", "")
    
    # API Keys
    COHERE_API_KEY: Optional[str] = os.getenv("COHERE_API_KEY")
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    QWEN_API_KEY: Optional[str] = os.getenv("QWEN_API_KEY")
    
    class Config:
        env_file = ".env"

settings = Settings()