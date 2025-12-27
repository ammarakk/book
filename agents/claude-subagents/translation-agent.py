from typing import Dict, Any
from .base_agent import BaseAgent


class TranslationAgent(BaseAgent):
    """
    Claude Code Subagent for generating English-Urdu translations while preserving technical accuracy
    """

    def get_agent_type(self) -> str:
        return "translation"

    def generate_prompt(self, original_content: str, user_context: Dict[str, Any], target_language: str = "ur") -> str:
        """
        Generate the prompt for the Claude API based on original content, user context, and target language
        """
        return f"""
        You are an expert translator specializing in technical content between English and {target_language}.
        Your task is to translate the following content while preserving technical accuracy and structure.

        RULES:
        1. Preserve all technical terminology (ROS 2, SLAM, URDF, Isaac Sim, etc.) - do not translate these
        2. Do NOT translate code blocks - keep them exactly as they are
        3. Preserve headings, lists, tables, and formatting structure
        4. Generate natural, professional {target_language} suitable for technical education
        5. Do NOT simplify concepts - maintain technical depth
        6. Do NOT add new examples, explanations, or summaries
        7. Do NOT remove warnings, notes, or constraints
        8. Ensure the translation is contextually accurate
        9. Maintain document structure (headings H1-H6, lists, paragraphs, etc.)
        10. Preserve any special formatting like bold, italic, or quoted text

        Original Content: {original_content}

        Please provide the translated content following these rules.
        """