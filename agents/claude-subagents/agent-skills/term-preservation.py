from typing import Dict, Any
from .base_skill import BaseSkill


class TechnicalTermPreservationSkill(BaseSkill):
    """
    Agent Skill for preserving technical terminology during translation
    """
    
    def get_skill_name(self) -> str:
        return "TechnicalTermPreservation"
    
    def execute(self, content: str, context: Dict[str, Any] = None) -> str:
        """
        Identify and mark technical terms in the content for preservation during translation
        """
        # In a real implementation, this would use NLP techniques to identify technical terms
        # For this implementation, we'll use a predefined list of common technical terms
        # in the domain of robotics and AI
        
        technical_terms = [
            "ROS", "ROS 2", "SLAM", "URDF", "Isaac Sim", "Isaac", "Sim", 
            "Gazebo", "Unity", "NVIDIA Isaac", "VLA", "Vision-Language-Action",
            "Qdrant", "Neon", "PostgreSQL", "FastAPI", "Claude", "Anthropic",
            "BetterAuth", "JWT", "API", "SDK", "IDE", "TCP/IP", "HTTP", "HTTPS",
            "JSON", "XML", "YAML", "Docker", "Kubernetes", "Git", "GitHub", "CI/CD",
            "SLAM", "PID", "PID controller", "PID Controller", "PID Controller",
            "LIDAR", "LiDAR", "IMU", "GPS", "Odometry", "Kinematics", "Dynamics",
            "Forward kinematics", "Inverse kinematics", "Path planning", "Motion planning",
            "Computer vision", "Machine learning", "Deep learning", "Neural network",
            "Reinforcement learning", "Supervised learning", "Unsupervised learning",
            "Transformer", "Attention mechanism", "Embedding", "Tokenization"
        ]
        
        # In a real implementation, we would mark these terms in the content
        # so that the translation agent knows not to translate them
        # For now, we'll just return the original content
        return content