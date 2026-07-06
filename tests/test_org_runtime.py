import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from engine.runtime import Runtime

def setup_dummy_org():
    base = "organizations/FrontendForce/v1"
    
    os.makedirs(f"{base}/capabilities/registry", exist_ok=True)
    os.makedirs(f"{base}/capabilities/FF.PROD.REQ", exist_ok=True)
    os.makedirs(f"{base}/capabilities/FF.UX.DESIGN", exist_ok=True)
    os.makedirs(f"{base}/roles", exist_ok=True)
    os.makedirs(f"{base}/protocols", exist_ok=True)
    
    with open(f"{base}/capabilities/registry/index.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"FF.PROD.REQ": {}, "FF.UX.DESIGN": {}}, f)
        
    with open(f"{base}/capabilities/FF.PROD.REQ/capability.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "FF.PROD.REQ", "name": "Requirements"}, f)
        
    with open(f"{base}/capabilities/FF.UX.DESIGN/capability.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "FF.UX.DESIGN", "name": "UX Design"}, f)
        
    with open(f"{base}/roles/ProductManager.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"name": "Product Manager"}, f)
        
    with open(f"{base}/protocols/FeatureDelivery.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"name": "Feature Delivery", "steps": ["FF.PROD.REQ", "FF.UX.DESIGN"]}, f)

def run():
    print("--- Setting up dummy org ---")
    setup_dummy_org()
    
    runtime = Runtime(".")
    
    print("\n--- Testing Exit Criteria ---")
    runtime.load_org("FrontendForce", "v1")
    runtime.execute_protocol("FrontendForce", "v1", "FeatureDelivery")

if __name__ == "__main__":
    run()
