from typing import Dict, Any, List

class ExecutionGraph:
    def __init__(self, organization: Dict[str, Any]):
        self.organization = organization

    def build_graph(self, protocol_id: str) -> List[str]:
        protocol = self.organization["protocols"].get(protocol_id)
        if not protocol:
            raise ValueError(f"Protocol '{protocol_id}' not found.")
            
        steps = protocol.get("steps", [])
        print(f"[Graph] Compiled execution graph for {protocol_id}: {steps}")
        return steps
