from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any
import time
import requests
from pydantic import BaseModel

from config import settings


router = APIRouter()


class HealthStatus(BaseModel):
    status: str
    timestamp: str
    services: Dict[str, str]


@router.get("/health", response_model=HealthStatus)
async def health_check():
    """
    Health check endpoint to verify the service is running and dependencies are accessible
    """
    # Check the status of various services
    services_status = {}

    # Check Ollama service
    try:
        response = requests.get(f"{settings.OLLAMA_BASE_URL}/api/tags", timeout=5)
        services_status["ollama"] = "available" if response.status_code == 200 else "unavailable"
    except:
        services_status["ollama"] = "unavailable"

    # Check Qdrant service
    try:
        # This is a simplified check - in practice, you'd check Qdrant's health endpoint
        from qdrant_client import QdrantClient
        client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        # Try to list collections as a basic connectivity test
        client.get_collections()
        services_status["qdrant"] = "available"
    except:
        services_status["qdrant"] = "unavailable"

    # Check Neon PostgreSQL connection
    try:
        import psycopg
        # Attempt to connect to the database
        with psycopg.connect(settings.NEON_DATABASE_URL, connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                services_status["postgres"] = "available"
    except:
        services_status["postgres"] = "unavailable"

    # Determine overall status based on service statuses
    overall_status = "healthy"
    if any(status == "unavailable" for status in services_status.values()):
        overall_status = "degraded"

    return {
        "status": overall_status,
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "services": services_status
    }


@router.get("/ready")
async def readiness_check():
    """
    Readiness check to verify the service is ready to accept traffic
    """
    # For now, just return that we're ready if health check passes
    # In the future, this could check for more specific readiness criteria
    health_status = await health_check()
    if health_status["status"] in ["healthy", "degraded"]:
        return {"status": "ready"}
    else:
        raise HTTPException(status_code=503, detail="Service not ready")