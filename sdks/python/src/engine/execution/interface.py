from abc import ABC, abstractmethod
from typing import Dict, Any

class ExecutionProvider(ABC):
    """
    Base interface for all execution backends (LLMs, Agents, Queues, CI).
    """
    @abstractmethod
    def submit(self, task_id: str, txf_payload: Dict[str, Any]) -> str:
        pass
        
    @abstractmethod
    def status(self, task_id: str) -> str:
        pass
