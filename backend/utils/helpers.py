"""
Utility functions for the Physical AI & Humanoid Robotics Book Chatbot
"""

import re
import logging
from typing import List, Dict, Any
from datetime import datetime


def setup_logging():
    """
    Set up logging configuration for the application
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('chatbot.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


def validate_book_reference(content: str) -> bool:
    """
    Validate that content references are to the Physical AI & Humanoid Robotics book
    """
    # This is a simplified validation - in practice, you'd check against the actual book content
    required_keywords = ["Physical AI", "Humanoid Robotics", "robot", "AI", "humanoid"]
    content_lower = content.lower()
    
    # Check if the content relates to the book topic
    for keyword in required_keywords:
        if keyword.lower() in content_lower:
            return True
    
    return False


def sanitize_input(user_input: str) -> str:
    """
    Sanitize user input to prevent injection attacks
    """
    # Remove potentially harmful characters/sequences
    sanitized = re.sub(r'<script[^>]*>.*?</script>', '', user_input, flags=re.IGNORECASE | re.DOTALL)
    sanitized = re.sub(r'javascript:', '', sanitized, flags=re.IGNORECASE)
    sanitized = sanitized.replace('<', '&lt;').replace('>', '&gt;')
    
    return sanitized.strip()


def format_source_citations(sources: List[str]) -> str:
    """
    Format source citations for display in chat responses
    """
    if not sources:
        return ""
    
    formatted_sources = []
    for source in sources:
        # Extract module/chapter information from source path
        # This is a simplified example - in practice, you'd have more sophisticated parsing
        if "/docs/module-" in source:
            parts = source.split("/")
            module_part = [p for p in parts if p.startswith("module-")][0] if any(p.startswith("module-") for p in parts) else "unknown-module"
            formatted_sources.append(f"- From {module_part.replace('-', ' ').title()}")
        else:
            formatted_sources.append(f"- From {source}")
    
    return "\nSources:\n" + "\n".join(formatted_sources)


def calculate_similarity_score(text1: str, text2: str) -> float:
    """
    Calculate a basic similarity score between two texts
    Note: This is a simplified implementation; in practice, you'd use embeddings for semantic similarity
    """
    # Convert to lowercase and tokenize
    tokens1 = set(text1.lower().split())
    tokens2 = set(text2.lower().split())
    
    # Calculate Jaccard similarity
    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)
    
    if not union:
        return 0.0
    
    return len(intersection) / len(union)


def extract_book_modules(content: str) -> List[str]:
    """
    Extract mentions of book modules from content
    """
    # Look for module references in the content
    module_pattern = r'(module\s+\d+|the\s+[\w\s]+system\s*\([^)]+\))'
    matches = re.findall(module_pattern, content, re.IGNORECASE)
    
    # Normalize the matches
    modules = []
    for match in matches:
        normalized = match.strip().lower()
        if normalized.startswith("module"):
            modules.append(normalized)
        elif "system" in normalized:
            modules.append(normalized)
    
    return list(set(modules))  # Return unique modules


def generate_response_template(context_available: bool = True) -> str:
    """
    Generate a response template based on whether context is available
    """
    if context_available:
        return (
            "Based on the Physical AI & Humanoid Robotics book:\n"
            "{answer}\n\n"
            "{sources}"
        )
    else:
        return (
            "I couldn't find this information in the Physical AI & Humanoid Robotics book. "
            "Please check the book content or try rephrasing your question."
        )


def log_chat_interaction(user_id: str, session_id: str, query: str, response: str, confidence: float):
    """
    Log chat interactions for analytics (without storing personal data)
    """
    logger = setup_logging()
    logger.info(f"Chat interaction - Session: {session_id}, "
                f"Confidence: {confidence:.2f}, "
                f"Query length: {len(query)}, "
                f"Response length: {len(response)}")


def validate_selected_text_context(question: str, selected_text: str) -> Dict[str, Any]:
    """
    Validate that the question is relevant to the selected text
    """
    result = {
        "valid": True,
        "message": "",
        "similarity_score": 0.0
    }
    
    if not selected_text or not question:
        result["valid"] = False
        result["message"] = "Both question and selected text are required"
        return result
    
    # Calculate similarity between question and selected text
    similarity = calculate_similarity_score(question, selected_text)
    result["similarity_score"] = similarity
    
    # If similarity is very low, the question might not relate to the selected text
    if similarity < 0.1:
        result["valid"] = False
        result["message"] = ("The question appears to be unrelated to the selected text. "
                             "Please ensure your question pertains to the highlighted content.")
    
    return result