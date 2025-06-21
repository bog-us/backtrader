"""Base interface for LLM integrations."""
from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """Abstract LLM provider."""

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate a response from the model."""
        raise NotImplementedError
