import os
from dotenv import load_dotenv

load_dotenv()

def validate_environment():
    """
    Validate that all required environment variables are set
    """
    required_vars = [
        "DATABASE_URL",
        "JWT_SECRET",
        "AUTH_SECRET"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    # Validate JWT_SECRET length
    jwt_secret = os.getenv("JWT_SECRET")
    if jwt_secret and len(jwt_secret) < 32:
        raise ValueError("JWT_SECRET should be at least 32 characters long for security")
    
    print("Environment validation passed")
    
# Call validation when module is imported
validate_environment()