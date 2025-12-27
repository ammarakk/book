from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseSkill(ABC):
    """
    Base class for Agent Skills that can be used by Claude Code Subagents
    """
    
    @abstractmethod
    def get_skill_name(self) -> str:
        """
        Return the name of the skill
        """
        pass
    
    @abstractmethod
    def execute(self, content: str, context: Dict[str, Any] = None) -> str:
        """
        Execute the skill on the given content with optional context
        """
        pass