from typing import Dict, Any
from .base_agent import BaseAgent


class IntermediateAgent(BaseAgent):
    """
    Claude Code Subagent for generating personalized content for users with intermediate-level backgrounds
    """

    def get_agent_type(self) -> str:
        return "intermediate"

    def generate_prompt(self, original_content: str, user_profile: Dict[str, Any]) -> str:
        """
        Generate the prompt for the Claude API based on original content and user profile
        """
        return f"""
        You are an expert educator helping intermediate-level users understand technical concepts.
        The user has an intermediate background in software and/or hardware as indicated in their profile.

        User Profile: {user_profile}

        Original Content: {original_content}

        Please generate explanations that are moderately detailed, with relevant examples.
        Include some technical depth but avoid overly complex jargon.
        The output should build on the user's existing knowledge while introducing new concepts.
        """