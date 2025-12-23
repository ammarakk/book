from fastapi import APIRouter

# Create main API router
api_router = APIRouter()

# Import and include other routers
from . import content_routes, auth_routes, user_routes, chat_routes, translation_routes

# Include routers with prefixes
api_router.include_router(content_routes.router, prefix="/content", tags=["content"])
api_router.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
api_router.include_router(user_routes.router, prefix="/users", tags=["users"])
api_router.include_router(chat_routes.router, prefix="/chat", tags=["chat"])
api_router.include_router(translation_routes.router, prefix="/translate", tags=["translation"])