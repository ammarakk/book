import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Authentication & User Profiles API is running"}

def test_signup_endpoint_exists():
    """Test that the signup endpoint exists"""
    response = client.post("/api/auth/signup", json={
        "email": "test@example.com",
        "password": "testpassword",
        "software_background": "beginner",
        "hardware_background": "none"
    })
    # This will likely return 409 (conflict) if user already exists or 422 (validation error) for invalid data
    # But it should not return 404 (not found)
    assert response.status_code in [409, 422, 400]

def test_signin_endpoint_exists():
    """Test that the signin endpoint exists"""
    response = client.post("/api/auth/signin", json={
        "email": "test@example.com",
        "password": "testpassword"
    })
    # This will likely return 401 (unauthorized) for invalid credentials
    # But it should not return 404 (not found)
    assert response.status_code in [401, 422, 400]