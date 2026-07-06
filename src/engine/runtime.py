from organization.loader import OrganizationLoader
from organization.graph import ExecutionGraph
from engine.event.bus import EventBus
from engine.task.engine import TaskEngine

class Runtime:
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.loader = OrganizationLoader(workspace_dir)
        self.bus = EventBus()
        self.task_engine = TaskEngine()
        self.org_cache = {}

    def load_org(self, org_name: str, version: str = "v1"):
        print(f"[Runtime] Loading Organization '{org_name}@{version}'...")
        org = self.loader.load_organization(org_name, version)
        self.org_cache[f"{org_name}@{version}"] = org
        print(f"[Runtime] Organization loaded successfully.")
        print(f"          Capabilities: {len(org['capabilities'])}")
        print(f"          Roles: {len(org['roles'])}")
        print(f"          Protocols: {len(org['protocols'])}")
        return org

    def execute_protocol(self, org_name: str, version: str, protocol_id: str):
        org_key = f"{org_name}@{version}"
        if org_key not in self.org_cache:
            self.load_org(org_name, version)
            
        org = self.org_cache[org_key]
        graph = ExecutionGraph(org)
        
        steps = graph.build_graph(protocol_id)
        
        print(f"\n[Runtime] Executing Protocol: {protocol_id}")
        for step in steps:
            print(f" -> [Step] Executing Capability: {step}")
            task = self.task_engine.create_task(f"Task for {step}", "Execute step", step)
            print(f"    [TaskEngine] Dispatched task {task.id}")
            
        print("[Runtime] Protocol execution finished.")
