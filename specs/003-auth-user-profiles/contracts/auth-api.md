# Authentication and Profile API Contracts

## Authentication Endpoints

### POST /api/auth/signup
**Description**: Register a new user with credentials and background information

**Request**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "software_background": "intermediate",
  "hardware_background": "robotics_experience"
}
```

**Response (201 Created)**:
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

**Validation**:
- Email must be valid format
- Password must be at least 8 characters
- Background fields must be from allowed enum values
- Email must be unique

**Errors**:
- 400: Invalid input data
- 409: Email already exists

### POST /api/auth/signin
**Description**: Authenticate existing user and return JWT token

**Request**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200 OK)**:
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "token": "jwt-token-string"
}
```

**Validation**:
- Email must exist
- Password must match stored hash

**Errors**:
- 400: Invalid input data
- 401: Invalid credentials

### POST /api/auth/logout
**Description**: Invalidate current user session

**Request**: (No body required, uses authentication header)

**Response (200 OK)**:
```json
{
  "message": "Successfully logged out"
}
```

**Errors**:
- 401: Invalid or expired token

### GET /api/auth/profile
**Description**: Retrieve current user's profile information

**Request**: (No body required, uses authentication header)

**Response (200 OK)**:
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

**Errors**:
- 401: Invalid or expired token

### PUT /api/auth/profile
**Description**: Update current user's profile information

**Request**:
```json
{
  "software_background": "advanced",
  "hardware_background": "robotics_experience"
}
```

**Response (200 OK)**:
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "profile": {
    "software_background": "advanced",
    "hardware_background": "robotics_experience"
  }
}
```

**Validation**:
- Background fields must be from allowed enum values

**Errors**:
- 400: Invalid input data
- 401: Invalid or expired token

## Protected Route Validation

### Middleware: authenticate
**Description**: Validates JWT token for protected endpoints

**Behavior**:
- Extracts token from Authorization header (Bearer token)
- Verifies token signature using stored secret
- Checks token expiration
- Attaches user information to request context

**Errors**:
- 401: Missing, invalid, or expired token