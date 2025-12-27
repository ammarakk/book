# Data Model: Authentication & User Profiles

## User Entity

### Fields
- **id**: UUID (Primary Key, auto-generated)
- **email**: String (Unique, required, valid email format)
- **hashed_password**: String (Required, bcrypt hashed)
- **created_at**: DateTime (Auto-generated timestamp)
- **updated_at**: DateTime (Auto-generated timestamp, updated on changes)

### Constraints
- Email must be unique
- Email must follow valid email format
- Password must be properly hashed (not stored in plain text)
- Created_at is set on creation only
- Updated_at is updated on any modification

### Validation Rules
- Email: Required, unique, valid format
- Password: Required, minimum 8 characters, stored as bcrypt hash

## User Profile Entity

### Fields
- **user_id**: UUID (Foreign Key to User.id, Primary Key)
- **software_background**: String (Required, enum: "beginner", "intermediate", "advanced")
- **hardware_background**: String (Required, enum: "none", "basic_electronics", "robotics_experience")
- **created_at**: DateTime (Auto-generated timestamp)
- **updated_at**: DateTime (Auto-generated timestamp, updated on changes)

### Constraints
- user_id must reference an existing User.id
- Each user can have only one profile record
- software_background and hardware_background are required fields

### Validation Rules
- user_id: Required, must reference existing user
- software_background: Required, must be one of the allowed values
- hardware_background: Required, must be one of the allowed values

## Relationships
- User (1) → (0 or 1) User Profile (One-to-zero-or-one)
- User Profile (1) → (1) User (One-to-one from profile perspective)

## State Transitions
- User: Created during signup, updated when profile is modified
- Profile: Created during signup, updated when user modifies their background information

## Indexes
- User.email: Unique index for fast lookups and uniqueness constraint
- User Profile.user_id: Index for fast foreign key lookups