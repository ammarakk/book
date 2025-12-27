from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.personalization import router as personalization_router

app = FastAPI(
    title="AI-Powered Content Personalization API",
    description="API for personalizing book content based on user background",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(personalization_router, prefix="/api/personalize", tags=["Personalization"])

@app.get("/")
def read_root():
    return {"message": "AI-Powered Content Personalization API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}