from typing import Dict, Any
from engine.knowledge.engine import KnowledgeEngine

class ContextBuilder:
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.knowledge_engine = KnowledgeEngine(workspace_dir)
        
    def build_task_context(self, task_id: str, capability_id: str, task_description: str = "") -> Dict[str, Any]:
        # RAG Retrieval
        query = f"{capability_id} {task_description}"
        retrieved_docs = self.knowledge_engine.retrieve(query=query)
        
        knowledge_context = ""
        if retrieved_docs:
            knowledge_context = f"RAG Retrieved: {retrieved_docs[0]['id']}"
        else:
            knowledge_context = "No specific knowledge found."

        return {
            "task_id": task_id,
            "capability_id": capability_id,
            "knowledge": knowledge_context,
            "workspace": self.workspace_dir
        }
