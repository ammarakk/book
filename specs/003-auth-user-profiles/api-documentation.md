# Authentication API Usage

## Base URL
All authentication endpoints are prefixed with `/api/auth`

## Endpoints

### POST /api/auth/signup
Register a new user with credentials and background information

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "software_background": "intermediate",
  "hardware_background": "robotics_experience"
}
```

**Response (200 OK):**
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "profile": {
    "software_background": "intermediate",
    "hardware_background": "robotics_experience"
  },
  "token": "jwt-token-string"
}
```

### POST /api/auth/signin
Authenticate existing user and return JWT token

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200 OK):**
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "token": "jwt-token-string"
}
```

### POST /api/auth/logout
Invalidate current user session

**Headers:**
```
Authorization: Bearer {token}
```

**Response (200 OK):**
```json
{
  "message": "Successfully logged out"
}
```

### GET /api/auth/profile
Retrieve current user's profile information

**Headers:**
```
Authorization: Bearer {token}
```

**Response (200 OK):**
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "profile": {
    "software_background": "intermediate",
    "hardware_background": "robotics_experience"
  }
}
```

### PUT /api/auth/profile
Update current user's profile information

**Headers:**
```
Authorization: Bearer {token}
```

**Request Body:**
```json
{
  "software_background": "advanced",
  "hardware_background": "robotics_experience"
}
```

**Response (200 OK):**
```json
{
  "user_id": "uuid-string",
  "profile": {
    "software_background": "advanced",
    "hardware_background": "robotics_experience"
  }
}
```

## Protected Endpoints

To access protected endpoints, include the JWT token in the Authorization header:

```
Authorization: Bearer {token}
```

Example protected endpoint: `GET /api/protected-example`