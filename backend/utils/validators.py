"""
Validation utilities for the Physical AI & Humanoid Robotics Book Chatbot
"""

from typing import Optional
from pydantic import BaseModel, validator, ValidationError
import re


class ChatQueryValidator:
    """
    Validator for chat queries to ensure they meet the requirements
    """
    
    @staticmethod
    def validate_question(question: str) -> bool:
        """
        Validate that a question is appropriate for the book chatbot
        """
        if not question or len(question.strip()) == 0:
            return False
        
        # Check for minimum length
        if len(question.strip()) < 3:
            return False
        
        # Check for maximum length
        if len(question) > 1000:
            return False
        
        # Check if question appears to be about the book topic
        question_lower = question.lower()
        book_related_terms = [
            "robot", "ai", "artificial intelligence", "humanoid", "physical ai", 
            "ros", "gazebo", "unity", "nvidia", "isaac", "vision", "language", 
            "action", "vla", "module", "chapter", "section"
        ]
        
        # At least one term should be present to be considered book-related
        is_book_related = any(term in question_lower for term in book_related_terms)
        
        return is_book_related
    
    @staticmethod
    def validate_selected_text(selected_text: str) -> bool:
        """
        Validate that selected text is appropriate for context selection mode
        """
        if not selected_text or len(selected_text.strip()) == 0:
            return False
        
        # Check for minimum length
        if len(selected_text.strip()) < 10:
            return False
        
        # Check for maximum length
        if len(selected_text) > 5000:  # Limit to 5000 characters
            return False
        
        return True


class ContentValidator:
    """
    Validator for book content to ensure it meets quality standards
    """
    
    @staticmethod
    def validate_content_chunk(content: str, source_module: str = "", source_chapter: str = "") -> dict:
        """
        Validate a content chunk before processing
        Returns a dictionary with validation results
        """
        result = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        if not content or len(content.strip()) == 0:
            result["valid"] = False
            result["errors"].append("Content cannot be empty")
            return result
        
        # Check content length
        if len(content) > 10000:  # More than 10k chars might be too large for a single chunk
            result["warnings"].append("Content chunk is very large, consider splitting it")
        
        # Check for book-specific content
        if source_module:
            if not re.match(r'^module-\d+[-\w]*$', source_module.lower().replace(' ', '-')):
                result["warnings"].append(f"Module name '{source_module}' doesn't follow expected pattern")
        
        if source_chapter:
            if len(source_chapter) < 2:
                result["warnings"].append("Chapter name seems too short")
        
        # Check for sensitive information
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.search(email_pattern, content):
            result["warnings"].append("Content contains potential email addresses")
        
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        if re.search(phone_pattern, content):
            result["warnings"].append("Content contains potential phone numbers")
        
        return result


class ResponseValidator:
    """
    Validator for chat responses to ensure they meet quality standards
    """
    
    @staticmethod
    def validate_response(answer: str, source_chunks: list, confidence_level: float) -> dict:
        """
        Validate a chat response before returning to user
        Returns a dictionary with validation results
        """
        result = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        if not answer or len(answer.strip()) == 0:
            result["valid"] = False
            result["errors"].append("Response cannot be empty")
        
        if not source_chunks:
            result["warnings"].append("Response has no source citations - may not be properly grounded in book content")
        
        if not (0 <= confidence_level <= 1):
            result["valid"] = False
            result["errors"].append("Confidence level must be between 0 and 1")
        
        # Check if response contains appropriate book-related content
        answer_lower = answer.lower()
        book_related_indicators = [
            "according to the book", "the text states", "based on the content", 
            "chapter", "module", "section", "refers to", "mentions", "describes"
        ]
        
        if not any(indicator in answer_lower for indicator in book_related_indicators) and source_chunks:
            result["warnings"].append("Response doesn't indicate it's based on book content despite having sources")
        
        # Check for potential hallucinations
        hallucination_indicators = [
            "i think", "i believe", "probably", "possibly", "might be", 
            "could be", "perhaps", "maybe", "in general", "usually"
        ]
        
        if any(indicator in answer_lower for indicator in hallucination_indicators):
            result["warnings"].append("Response contains uncertain language that might indicate hallucination")
        
        return result


class SessionValidator:
    """
    Validator for chat sessions
    """
    
    @staticmethod
    def validate_session_id(session_id: str) -> bool:
        """
        Validate a session ID format
        """
        if not session_id:
            return False
        
        # Basic validation: alphanumeric, hyphens, underscores, between 5 and 64 characters
        pattern = r'^[a-zA-Z0-9_-]{5,64}$'
        return bool(re.match(pattern, session_id))


# Custom Pydantic validators for request models
def validate_question_field(question: str) -> str:
    """
    Validator for question field in request models
    """
    if not ChatQueryValidator.validate_question(question):
        raise ValueError("Question must be at least 3 characters, less than 1000 characters, and related to the book content")
    return question


def validate_selected_text_field(selected_text: str) -> str:
    """
    Validator for selected text field in request models
    """
    if selected_text and not ChatQueryValidator.validate_selected_text(selected_text):
        raise ValueError("Selected text must be between 10 and 5000 characters if provided")
    return selected_text


def validate_confidence_level(confidence: float) -> float:
    """
    Validator for confidence level field
    """
    if not (0 <= confidence <= 1):
        raise ValueError("Confidence level must be between 0 and 1")
    return confidence