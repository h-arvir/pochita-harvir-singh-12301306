"""
Conversation Manager - Tracks and formats agent interactions
Custom class to maintain conversation history and context
"""

from typing import List, Dict
from datetime import datetime


class ConversationManager:
    """Manages conversation history between agents and user"""
    
    def __init__(self):
        self.history: List[Dict] = []
    
    def add_message(self, role: str, content: str, agent_type: str = None):
        """Add a message to conversation history"""
        message = {
            "timestamp": datetime.now().isoformat(),
            "role": role,  # "user", "coder", "tester", "system"
            "content": content,
            "agent_type": agent_type
        }
        self.history.append(message)
        return message
    
    def get_history(self) -> List[Dict]:
        """Get full conversation history"""
        return self.history
    
    def get_context(self, limit: int = 5) -> str:
        """Get formatted context for LLM (last N messages)"""
        recent = self.history[-limit:]
        context = "\n".join([
            f"{msg['role'].upper()}: {msg['content']}"
            for msg in recent
        ])
        return context
    
    def clear(self):
        """Clear conversation history"""
        self.history = []