from dotenv import load_dotenv
import os

load_dotenv()

# BetterAuth configuration
AUTH_SECRET = os.getenv("AUTH_SECRET", "your-default-auth-secret-change-in-production")
JWT_SECRET = os.getenv("JWT_SECRET", "your-default-jwt-secret-change-in-production")

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# JWT Configuration
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7