from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Generator

class Provider(ABC):
    """
    Abstract base class defining the standard interface for all AI Reasoning Providers 
    (e.g., Claude, Gemini, OpenAI, Ollama).
    
    The Reasoning Engine uses this interface to interact with models agnostically,
    ensuring Continuum is not tightly coupled to any single LLM API.
    """

    def __init__(self, api_key: str, model_name: str, **kwargs):
        self.api_key = api_key
        self.model_name = model_name
        self.config = kwargs

    @abstractmethod
    def chat(self, messages: List[Dict[str, str]], system_prompt: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Sends a complete chat payload to the provider and returns the full response.
        
        Args:
            messages: List of message dicts with 'role' and 'content'.
            system_prompt: Optional system-level instructions.
            **kwargs: Additional provider-specific parameters (e.g., temperature).
            
        Returns:
            A dictionary containing the response text and metadata (e.g., token usage).
        """
        pass

    @abstractmethod
    def stream(self, messages: List[Dict[str, str]], system_prompt: Optional[str] = None, **kwargs) -> Generator[str, None, None]:
        """
        Sends a chat payload and yields the response as a stream of text chunks.
        
        Args:
            messages: List of message dicts with 'role' and 'content'.
            system_prompt: Optional system-level instructions.
            **kwargs: Additional provider-specific parameters.
            
        Yields:
            Text chunks as they arrive from the API.
        """
        pass

    @abstractmethod
    def embeddings(self, texts: List[str], **kwargs) -> List[List[float]]:
        """
        Converts a list of text strings into high-dimensional embedding vectors.
        This is heavily used by the Knowledge Engine for semantic search.
        
        Args:
            texts: List of strings to embed.
            **kwargs: Additional provider-specific parameters.
            
        Returns:
            A list of embedding vectors (list of floats) corresponding to the input texts.
        """
        pass

class ProviderRegistry:
    """
    Manages registration and instantiation of different AI Providers.
    """
    _providers = {}

    @classmethod
    def register(cls, name: str, provider_class: type):
        cls._providers[name] = provider_class

    @classmethod
    def get_provider(cls, name: str, api_key: str, model_name: str, **kwargs) -> Provider:
        if name not in cls._providers:
            raise ValueError(f"Provider '{name}' is not registered.")
        return cls._providers[name](api_key=api_key, model_name=model_name, **kwargs)
