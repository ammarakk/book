import requests
from typing import Optional
from src.config import settings


class OllamaService:
    """
    Service to interact with Ollama API for AI responses.
    """
    
    def __init__(self):
        self.ollama_url = settings.OLLAMA_URL
        self.model = "llama3"  # Default model
    
    def generate_response(self, user_message: str, context: Optional[str] = None) -> str:
        """
        Generate a response using the Ollama API.
        """
        # Prepare the prompt with context if available
        if context:
            prompt = f"Context: {context}\n\nQuestion: {user_message}\n\nAnswer:"
        else:
            prompt = f"Question: {user_message}\n\nAnswer:"
        
        # Prepare the request payload
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            # Make request to Ollama API
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "I couldn't generate a response at this time.")
            else:
                return f"Error from Ollama: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error calling Ollama API: {str(e)}"