from typing import Dict, Any
from .base_agent import BaseAgent


class BeginnerAgent(BaseAgent):
    """
    Claude Code Subagent for generating personalized content for users with beginner-level backgrounds
    """

    def get_agent_type(self) -> str:
        return "beginner"

    def generate_prompt(self, original_content: str, user_profile: Dict[str, Any]) -> str:
        """
        Generate the prompt for the Claude API based on original content and user profile
        """
        return f"""
        You are an expert educator helping beginners understand complex technical concepts.
        The user has a beginner background in software and/or hardware as indicated in their profile.

        User Profile: {user_profile}

        Original Content: {original_content}

        Please generate simplified explanations and examples that would be appropriate for a beginner.
        Use analogies, simple language, and step-by-step explanations.
        Ensure technical terms are explained in simple terms.
        The output should help the user understand the concept without overwhelming them.
        """