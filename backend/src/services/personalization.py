from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid
import jwt
from ..config.personalization import config

from ..models.personalization import (
    PersonalizationSession,
    PersonalizationSessionCreate,
    PersonalizedContent,
    PersonalizedContentCreate
)


class PersonalizationService:
    """
    Service class for handling personalization logic
    """

    # In-memory storage for demonstration purposes
    # In a real implementation, this would use a database
    sessions: Dict[str, PersonalizationSession] = {}
    contents: Dict[str, List[PersonalizedContent]] = {}

    @classmethod
    def verify_user_authentication(cls, token: str, expected_user_id: str) -> bool:
        """
        Verify that the user is authenticated and owns the session
        """
        try:
            # Decode the JWT token using the secret from config
            payload = jwt.decode(
                token,
                config.jwt_secret,
                algorithms=["HS256"]
            )

            # Check if the user ID in the token matches the expected user ID
            token_user_id = payload.get("sub")
            return token_user_id == expected_user_id

        except jwt.ExpiredSignatureError:
            print("Token has expired")
            return False
        except jwt.JWTError:
            print("Invalid token")
            return False
        except Exception as e:
            print(f"Error verifying token: {e}")
            return False

    @classmethod
    def create_session(cls, session_data: PersonalizationSessionCreate) -> PersonalizationSession:
        """
        Create a new personalization session
        """
        session = PersonalizationSession(
            session_id=str(uuid.uuid4()),
            user_id=session_data.user_id,
            chapter_id=session_data.chapter_id,
            user_profile=session_data.user_profile,
            personalization_state=session_data.personalization_state,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        cls.sessions[session.session_id] = session
        cls.contents[session.session_id] = []

        return session

    @classmethod
    def get_session(cls, session_id: str) -> Optional[PersonalizationSession]:
        """
        Get a personalization session by ID
        """
        return cls.sessions.get(session_id)

    @classmethod
    def update_session(cls, session_id: str, update_data) -> Optional[PersonalizationSession]:
        """
        Update a personalization session
        """
        if session_id not in cls.sessions:
            return None

        session = cls.sessions[session_id]
        if update_data.personalization_state is not None:
            session.personalization_state = update_data.personalization_state
            session.updated_at = datetime.now()

        return session

    @classmethod
    def create_content(cls, content_data: PersonalizedContentCreate) -> PersonalizedContent:
        """
        Create personalized content
        """
        content = PersonalizedContent(
            content_id=str(uuid.uuid4()),
            session_id=content_data.session_id,
            original_content_id=content_data.original_content_id,
            personalized_text=content_data.personalized_text,
            personalization_type=content_data.personalization_type,
            user_background_level=content_data.user_background_level,
            created_at=datetime.now()
        )

        if content.session_id not in cls.contents:
            cls.contents[content.session_id] = []

        cls.contents[content.session_id].append(content)
        return content

    @classmethod
    def get_contents_by_session(cls, session_id: str) -> List[PersonalizedContent]:
        """
        Get all personalized content for a session
        """
        return cls.contents.get(session_id, [])

    @classmethod
    def generate_personalized_content(
        cls,
        session_id: str,
        chapter_id: str,
        user_background: Dict[str, Any]
    ) -> List[PersonalizedContent]:
        """
        Generate personalized content using Claude Code Subagents
        """
        # This is a simplified implementation
        # In a real implementation, this would call the Claude Code Subagents

        # For demonstration, we'll create some mock personalized content
        mock_contents = []

        # Example: Create different types of personalized content based on user background
        if user_background.get("software_background") == "beginner":
            explanation_content = PersonalizedContentCreate(
                session_id=session_id,
                original_content_id=f"{chapter_id}-intro",
                personalized_text=f"As a beginner in software development, think of {chapter_id} as a fundamental building block. It's like learning the alphabet before writing sentences.",
                personalization_type="explanation",
                user_background_level="beginner"
            )
            mock_contents.append(explanation_content)

            example_content = PersonalizedContentCreate(
                session_id=session_id,
                original_content_id=f"{chapter_id}-example",
                personalized_text=f"For beginners, here's a simplified example of {chapter_id}: # Simple example code for beginners",
                personalization_type="example",
                user_background_level="beginner"
            )
            mock_contents.append(example_content)

        elif user_background.get("software_background") == "advanced":
            explanation_content = PersonalizedContentCreate(
                session_id=session_id,
                original_content_id=f"{chapter_id}-intro",
                personalized_text=f"As an advanced developer, you'll appreciate that {chapter_id} implements sophisticated patterns like dependency injection and reactive programming.",
                personalization_type="explanation",
                user_background_level="advanced"
            )
            mock_contents.append(explanation_content)

        # Create actual content objects
        created_contents = []
        for content_data in mock_contents:
            created_content = cls.create_content(content_data)
            created_contents.append(created_content)

        return created_contents