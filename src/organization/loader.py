import os
import yaml
from typing import Dict, Any

class OrganizationLoader:
    """
    Loads organizations and their capability registries from the file system.
    This parses the organization graph into a structured object for the runtime.
    """
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.orgs_dir = os.path.join(workspace_dir, "organizations")
    
    def load_organization(self, org_name: str, version: str = "v1") -> Dict[str, Any]:
        """Loads an organization's capabilities and registry."""
        org_path = os.path.join(self.orgs_dir, org_name, version)
        if not os.path.exists(org_path):
            raise FileNotFoundError(f"Organization '{org_name}' not found at {org_path}")
        
        # Load registry index
        registry_path = os.path.join(org_path, "capabilities", "registry", "index.yaml")
        registry = {}
        if os.path.exists(registry_path):
            with open(registry_path, "r") as f:
                registry = yaml.safe_load(f) or {}
                
        # Load individual capabilities dynamically
        capabilities_dir = os.path.join(org_path, "capabilities")
        capabilities = {}
        if os.path.exists(capabilities_dir):
            for item in os.listdir(capabilities_dir):
                cap_dir = os.path.join(capabilities_dir, item)
                if os.path.isdir(cap_dir):
                    cap_file = os.path.join(cap_dir, "capability.yaml")
                    if os.path.exists(cap_file):
                        with open(cap_file, "r") as f:
                            capabilities[item] = yaml.safe_load(f)
                            
        return {
            "name": org_name,
            "version": version,
            "registry": registry,
            "capabilities": capabilities
        }
