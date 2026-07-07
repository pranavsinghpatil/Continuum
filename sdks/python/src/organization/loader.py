import os
import yaml
from typing import Dict, Any

class OrganizationLoader:
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.orgs_dir = os.path.join(workspace_dir, "organizations")
    
    def load_organization(self, org_name: str, version: str = "v1") -> Dict[str, Any]:
        org_path = os.path.join(self.orgs_dir, org_name, version)
        if not os.path.exists(org_path):
            raise FileNotFoundError(f"Organization '{org_name}' not found at {org_path}")
        
        # Load registry index
        registry_path = os.path.join(org_path, "capabilities", "registry", "index.yaml")
        registry = {}
        if os.path.exists(registry_path):
            with open(registry_path, "r", encoding="utf-8") as f:
                registry = yaml.safe_load(f) or {}
                
        # Load capabilities
        capabilities_dir = os.path.join(org_path, "capabilities")
        capabilities = {}
        if os.path.exists(capabilities_dir):
            for item in os.listdir(capabilities_dir):
                if item == "registry": continue
                cap_dir = os.path.join(capabilities_dir, item)
                if os.path.isdir(cap_dir):
                    cap_file = os.path.join(cap_dir, "capability.yaml")
                    if os.path.exists(cap_file):
                        with open(cap_file, "r", encoding="utf-8") as f:
                            capabilities[item] = yaml.safe_load(f)

        # Load roles
        roles_dir = os.path.join(org_path, "roles")
        roles = {}
        if os.path.exists(roles_dir):
            for item in os.listdir(roles_dir):
                if item.endswith(".yaml"):
                    with open(os.path.join(roles_dir, item), "r", encoding="utf-8") as f:
                        role_id = item.replace(".yaml", "")
                        roles[role_id] = yaml.safe_load(f)

        # Load protocols
        protocols_dir = os.path.join(org_path, "protocols")
        protocols = {}
        if os.path.exists(protocols_dir):
            for item in os.listdir(protocols_dir):
                if item.endswith(".yaml"):
                    with open(os.path.join(protocols_dir, item), "r", encoding="utf-8") as f:
                        protocol_id = item.replace(".yaml", "")
                        protocols[protocol_id] = yaml.safe_load(f)

        return {
            "name": org_name,
            "version": version,
            "registry": registry,
            "capabilities": capabilities,
            "roles": roles,
            "protocols": protocols
        }
