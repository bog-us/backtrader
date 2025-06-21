"""FinRobot model integration."""

from .base import LLMProvider


class FinRobot(LLMProvider):
    """Stub implementation of FinRobot integration."""

    def generate_response(self, prompt: str) -> str:
        """Generate a response using FinRobot (placeholder)."""
        # Real implementation would call the FinRobot API
        return f"FinRobot response to: {prompt}"
