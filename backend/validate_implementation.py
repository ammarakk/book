# Quickstart validation for the Personalization Engine

print("Validating Personalization Engine Implementation...")

# 1. Check that all required files exist
import os

required_files = [
    "../docusaurus/src/components/PersonalizeButton.js",
    "../docusaurus/src/components/PersonalizedContent.js",
    "../docusaurus/src/services/personalization.js",
    "../docusaurus/src/css/personalization.css",
    "src/api/personalization.py",
    "src/services/personalization.py",
    "src/models/personalization.py",
    "src/config/personalization.py",
    "../agents/claude-subagents/beginner-agent.py",
    "../agents/claude-subagents/intermediate-agent.py",
    "../agents/claude-subagents/advanced-agent.py",
    "../agents/claude-subagents/agent-skills/simplification.py",
    "../agents/claude-subagents/agent-skills/elaboration.py",
    "../agents/claude-subagents/agent-skills/terminology-check.py"
]

missing_files = []
for file in required_files:
    if not os.path.exists(file):
        missing_files.append(file)

if missing_files:
    print(f"[ERROR] Missing required files: {missing_files}")
else:
    print("[SUCCESS] All required files exist")

# 2. Check that the Claude Code Subagent base framework exists
try:
    import sys
    sys.path.insert(0, '../agents')
    from claude_subagents.base_agent import BaseAgent
    print("[SUCCESS] Claude Code Subagent base framework exists")
except ImportError as e:
    print(f"[ERROR] Could not import Claude Code Subagent base framework: {e}")

# 3. Check that the Agent Skills base framework exists
try:
    from claude_subagents.agent_skills.base_skill import BaseSkill
    print("[SUCCESS] Agent Skills base framework exists")
except ImportError as e:
    print(f"[ERROR] Could not import Agent Skills base framework: {e}")

# 4. Check that the personalization models exist and are importable
try:
    sys.path.append('.')
    from src.models.personalization import PersonalizationSession, PersonalizedContent
    print("[SUCCESS] Personalization models exist and are importable")
except ImportError as e:
    print(f"[ERROR] Could not import personalization models: {e}")

# 5. Check that the personalization service exists and is importable
try:
    from src.services.personalization import PersonalizationService
    print("[SUCCESS] Personalization service exists and is importable")
except ImportError as e:
    print(f"[ERROR] Could not import personalization service: {e}")

# 6. Check that the personalization API exists and is importable
try:
    from src.api.personalization import router
    print("[SUCCESS] Personalization API exists and is importable")
except ImportError as e:
    print(f"[ERROR] Could not import personalization API: {e}")

# 7. Check that the configuration exists and is importable
try:
    from src.config.personalization import config
    print("[SUCCESS] Personalization configuration exists and is importable")
except ImportError as e:
    print(f"[ERROR] Could not import personalization configuration: {e}")

print("\nQuickstart validation complete!")