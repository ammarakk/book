import os
import requests
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import json


class BaseAgent(ABC):
    """
    Base class for Claude Code Subagents that handle translation tasks
    """
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("CLAUDE_API_KEY")
        if not self.api_key:
            raise ValueError("CLAUDE_API_KEY must be provided either as parameter or environment variable")
        
        self.base_url = os.getenv("CLAUDE_API_BASE_URL", "https://api.anthropic.com/v1/messages")
        self.headers = {
            "x-api-key": self.api_key,
            "content-type": "application/json",
            "anthropic-version": os.getenv("CLAUDE_API_VERSION", "2023-06-01")
        }
    
    @abstractmethod
    def get_agent_type(self) -> str:
        """
        Return the type of agent (e.g., "translation", "personalization", etc.)
        """
        pass
    
    @abstractmethod
    def generate_prompt(self, original_content: str, user_context: Dict[str, Any]) -> str:
        """
        Generate the prompt for the Claude API based on original content and user context
        """
        pass
    
    def call_claude_api(self, prompt: str, max_tokens: int = 1000) -> Optional[str]:
        """
        Call the Claude API with the given prompt
        """
        payload = {
            "model": os.getenv("CLAUDE_DEFAULT_MODEL", "claude-3-opus-20240229"),
            "max_tokens": max_tokens,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            
            result = response.json()
            return result['content'][0]['text']  # Extract the generated text
            
        except requests.exceptions.RequestException as e:
            print(f"Error calling Claude API: {e}")
            return None
        except KeyError:
            print("Unexpected response format from Claude API")
            return None
    
    def process_content(self, original_content: str, user_context: Dict[str, Any]) -> Optional[str]:
        """
        Main method to process content using Claude API
        """
        prompt = self.generate_prompt(original_content, user_context)
        return self.call_claude_api(prompt)