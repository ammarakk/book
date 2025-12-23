from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import api_router
from src.config import settings

app = FastAPI(title="AI-Driven Physical AI & Humanoid Robotics Book Platform API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api", tags=["api"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Physical AI & Humanoid Robotics Book Platform API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Include other routes as needed