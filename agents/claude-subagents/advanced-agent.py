from typing import Dict, Any
from .base_agent import BaseAgent


class AdvancedAgent(BaseAgent):
    """
    Claude Code Subagent for generating personalized content for users with advanced-level backgrounds
    """

    def get_agent_type(self) -> str:
        return "advanced"

    def generate_prompt(self, original_content: str, user_profile: Dict[str, Any]) -> str:
        """
        Generate the prompt for the Claude API based on original content and user profile
        """
        return f"""
        You are an expert educator helping advanced users understand complex technical concepts.
        The user has an advanced background in software and/or hardware as indicated in their profile.

        User Profile: {user_profile}

        Original Content: {original_content}

        Please generate detailed, technical explanations with complex examples.
        Include advanced terminology and assume deep understanding of fundamentals.
        The output should provide sophisticated insights and advanced applications of the concepts.
        """