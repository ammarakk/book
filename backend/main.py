from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import API routers
from src.api.auth import router as auth_router
from src.api.profile import router as profile_router
from src.api.protected import router as protected_router
from src.api.personalization import router as personalization_router

# Create FastAPI app
app = FastAPI(title="Authentication & User Profiles API", version="1.0.0")

# Add CORS middleware (adjust origins as needed for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(profile_router, prefix="/api/auth", tags=["Profile"])
app.include_router(personalization_router, prefix="/api/personalize", tags=["Personalization"])
app.include_router(protected_router, prefix="/api", tags=["Protected"])

@app.get("/")
def read_root():
    return {"message": "Authentication & User Profiles API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)