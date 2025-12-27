#!/usr/bin/env python
"""
Backend server for the Physical AI & Humanoid Robotics Book Project
Phase 4: AI-Powered Content Personalization
"""

import uvicorn
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Get host and port from environment or use defaults
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    print(f"Starting backend server on {host}:{port}")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run(
        "main:app",  # This refers to the 'app' object in main.py
        host=host,
        port=port,
        reload=True,  # Auto-reload on code changes (development only)
        log_level="info"
    )