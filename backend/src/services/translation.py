from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid
import jwt
from ..config.translation import config


class TranslationService:
    """
    Service class for handling translation logic
    """

    # In-memory storage for demonstration purposes
    # In a real implementation, this would use a database
    sessions: Dict[str, TranslationSession] = {}
    contents: Dict[str, List[TranslatedContent]] = {}

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
    def create_session(cls, session_data: TranslationSessionCreate) -> TranslationSession:
        """
        Create a new translation session
        """
        session = TranslationSession(
            session_id=str(uuid.uuid4()),
            user_id=session_data.user_id,
            chapter_id=session_data.chapter_id,
            source_language=session_data.source_language,
            target_language=session_data.target_language,
            translation_state=session_data.translation_state,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        cls.sessions[session.session_id] = session
        cls.contents[session.session_id] = []
        
        return session

    @classmethod
    def get_session(cls, session_id: str) -> Optional[TranslationSession]:
        """
        Get a translation session by ID
        """
        return cls.sessions.get(session_id)

    @classmethod
    def update_session(cls, session_id: str, update_data) -> Optional[TranslationSession]:
        """
        Update a translation session
        """
        if session_id not in cls.sessions:
            return None
            
        session = cls.sessions[session_id]
        if update_data.translation_state is not None:
            session.translation_state = update_data.translation_state
            session.updated_at = datetime.now()
            
        return session

    @classmethod
    def create_content(cls, content_data: TranslatedContentCreate) -> TranslatedContent:
        """
        Create translated content
        """
        content = TranslatedContent(
            content_id=str(uuid.uuid4()),
            session_id=content_data.session_id,
            original_content_id=content_data.original_content_id,
            original_text=content_data.original_text,
            translated_text=content_data.translated_text,
            content_type=content_data.content_type,
            preservation_flags=content_data.preservation_flags,
            created_at=datetime.now()
        )
        
        if content.session_id not in cls.contents:
            cls.contents[content.session_id] = []
        
        cls.contents[content.session_id].append(content)
        return content

    @classmethod
    def get_contents_by_session(cls, session_id: str) -> List[TranslatedContent]:
        """
        Get all translated content for a session
        """
        return cls.contents.get(session_id, [])

    @classmethod
    def generate_translated_content(
        cls, 
        session_id: str, 
        chapter_id: str, 
        target_language: str
    ) -> List[TranslatedContent]:
        """
        Generate translated content using Claude Code Subagents
        """
        # This is a simplified implementation
        # In a real implementation, this would call the Claude Code Subagents
        
        # For demonstration, we'll create some mock translated content
        mock_contents = []
        
        # Example: Create different types of translated content
        explanation_content = TranslatedContentCreate(
            session_id=session_id,
            original_content_id=f"{chapter_id}-intro",
            original_text="In robotics, the Robot Operating System (ROS) provides a framework for writing robot software...",
            translated_text="روبوٹکس میں، روبوٹ آپریٹنگ سسٹم (ROS) روبوٹ سافٹ ویئر لکھنے کے لیے ایک فریم ورک فراہم کرتا ہے...",
            content_type="text",
            preservation_flags='{"technical_terms": ["ROS"], "code_elements": []}'
        )
        mock_contents.append(explanation_content)
        
        code_example_content = TranslatedContentCreate(
            session_id=session_id,
            original_content_id=f"{chapter_id}-code-example",
            original_text="# This is a ROS publisher example\nros::Publisher pub = n.advertise<std_msgs::String>(\"chatter\", 1000);",
            translated_text="# یہ ایک ROS پبلشر کی مثال ہے\nros::Publisher pub = n.advertise<std_msgs::String>(\"chatter\", 1000);",  # Code blocks remain unchanged
            content_type="code_block",
            preservation_flags='{"technical_terms": [], "code_elements": ["ros::Publisher pub = n.advertise<std_msgs::String>(\"chatter\", 1000);"]}'
        )
        mock_contents.append(code_example_content)
        
        # Create actual content objects
        created_contents = []
        for content_data in mock_contents:
            created_content = cls.create_content(content_data)
            created_contents.append(created_content)
        
        return created_contents