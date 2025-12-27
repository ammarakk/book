# Quickstart: Authentication & User Profiles

## Prerequisites

- Python 3.11+
- Node.js 18+ (for Docusaurus frontend)
- Neon Serverless PostgreSQL database
- BetterAuth account/config (or self-hosted instance)

## Environment Setup

1. **Database Setup**:
   ```bash
   # Create Neon Serverless PostgreSQL database
   # Get your database connection string from Neon dashboard
   ```

2. **Environment Variables**:
   ```bash
   # backend/.env
   DATABASE_URL="your-neon-db-connection-string"
   JWT_SECRET="your-jwt-secret-key"
   AUTH_SECRET="your-auth-secret"
   ```

## Backend Setup

1. **Install Dependencies**:
   ```bash
   cd backend
   pip install fastapi uvicorn better-auth bcrypt python-jose[cryptography]
   ```

2. **Database Migration**:
   ```bash
   # Run database migrations to create users and profiles tables
   python -m src.database.migrate
   ```

3. **Start Backend**:
   ```bash
   cd backend
   uvicorn src.main:app --reload --port 8000
   ```

## Frontend Setup

1. **Install Dependencies**:
   ```bash
   cd docusaurus
   npm install
   ```

2. **Start Frontend**:
   ```bash
   cd docusaurus
   npm start
   ```

## API Endpoints

- **Auth Signup**: `POST http://localhost:8000/api/auth/signup`
- **Auth Signin**: `POST http://localhost:8000/api/auth/signin`
- **Auth Logout**: `POST http://localhost:8000/api/auth/logout`
- **Get Profile**: `GET http://localhost:8000/api/auth/profile`
- **Update Profile**: `PUT http://localhost:8000/api/auth/profile`

## Testing Authentication Flow

1. **Sign up a new user**:
   ```bash
   curl -X POST http://localhost:8000/api/auth/signup \
     -H "Content-Type: application/json" \
     -d '{
       "email": "test@example.com",
       "password": "securePassword123",
       "software_background": "intermediate",
       "hardware_background": "robotics_experience"
     }'
   ```

2. **Sign in**:
   ```bash
   curl -X POST http://localhost:8000/api/auth/signin \
     -H "Content-Type: application/json" \
     -d '{
       "email": "test@example.com",
       "password": "securePassword123"
     }'
   ```

3. **Access protected endpoint** (use the token from signin response):
   ```bash
   curl -X GET http://localhost:8000/api/auth/profile \
     -H "Authorization: Bearer YOUR_JWT_TOKEN"
   ```

## Frontend Integration

The authentication state is managed through React context:

```javascript
// Use the AuthProvider to wrap your application
import { AuthProvider } from './components/AuthProvider';

function App() {
  return (
    <AuthProvider>
      {/* Your application components */}
    </AuthProvider>
  );
}

// Access authentication state in components
import { useAuth } from './components/AuthProvider';

function MyComponent() {
  const { user, isAuthenticated, login, logout } = useAuth();
  
  if (!isAuthenticated) {
    return <div>Please sign in</div>;
  }
  
  return <div>Welcome, {user.email}!</div>;
}
```