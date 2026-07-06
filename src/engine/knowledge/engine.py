import os
import json
from typing import List, Dict, Any

class KnowledgeEngine:
    def __init__(self, workspace_dir: str = "."):
        self.knowledge_dir = os.path.join(workspace_dir, "knowledge")
        self.documents = []
        self._build_index()

    def _build_index(self):
        if not os.path.exists(self.knowledge_dir):
            return
            
        for root, _, files in os.walk(self.knowledge_dir):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        self.documents.append({
                            "id": file,
                            "path": path,
                            "content": content
                        })

    def retrieve(self, query: str, top_k: int = 1) -> List[Dict[str, Any]]:
        # Mock RAG Keyword Ranking
        results = []
        query_words = set(query.lower().replace(".", " ").split())
        
        for doc in self.documents:
            content_words = set(doc["content"].lower().split())
            doc_id_words = set(doc["id"].lower().replace(".md", "").split())
            
            # Match against content and filename
            overlap = len(query_words.intersection(content_words)) + (len(query_words.intersection(doc_id_words)) * 2)
            results.append((overlap, doc))
            
        results.sort(key=lambda x: x[0], reverse=True)
        return [res[1] for res in results[:top_k] if res[0] > 0]
