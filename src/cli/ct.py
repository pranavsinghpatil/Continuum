import os
import sys
import yaml
import argparse

# Add src directory to path to allow importing internal modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from config.parser import load_config, ConfigError
except ImportError:
    pass

VERSION = "0.1.0"

def init_workspace(project_name):
    print(f"Initializing Continuum workspace in '{project_name}'...")
    base_dir = os.path.join(os.getcwd(), project_name)
    
    dirs = [
        ".continuum",
        "organizations",
        "knowledge",
        ".artifacts",
        ".history"
    ]
    
    try:
        for d in dirs:
            os.makedirs(os.path.join(base_dir, d), exist_ok=True)
            
        config_path = os.path.join(base_dir, "continuum.yaml")
        if not os.path.exists(config_path):
            config = {
                "project": project_name,
                "continuum_version": VERSION,
                "engines": {
                    "reasoning": "default",
                    "knowledge": "default",
                    "workflow": "default",
                    "governance": "default"
                }
            }
            with open(config_path, "w", encoding="utf-8") as f:
                yaml.dump(config, f, sort_keys=False)
                
        print(f"[OK] Continuum workspace created successfully in ./{project_name}")
    except Exception as e:
        print(f"[ERROR] Error creating workspace: {e}")

def doctor():
    """Checks the health of the Continuum environment."""
    print("[INFO] Running Continuum Doctor...")
    issues = 0
    
    if not os.path.exists("continuum.yaml"):
        print("[ERROR] Not in a valid Continuum workspace (missing continuum.yaml)")
        issues += 1
    else:
        print("[OK] Found continuum.yaml")
        
    for d in [".continuum", "organizations", "knowledge", ".artifacts", ".history"]:
        if os.path.exists(d):
            print(f"[OK] Directory {d} exists")
        else:
            print(f"[ERROR] Missing directory: {d}")
            issues += 1
            
    if issues == 0:
        print("[SUCCESS] Environment is healthy!")
    else:
        print(f"[WARN] Found {issues} issues.")

def validate():
    """Validates the continuum.yaml and loaded configuration."""
    print("[INFO] Validating workspace configuration...")
    try:
        from config.parser import load_config
        config = load_config(".")
        print("[OK] Configuration is valid!")
        print(f"Project: {config.project_name}")
        print(f"Version: {config.version}")
    except Exception as e:
        print(f"[ERROR] Validation failed: {e}")

def print_config():
    """Prints the currently loaded configuration."""
    try:
        from config.parser import load_config
        config = load_config(".")
        print(f"Project: {config.project_name}")
        print(f"Continuum Version: {config.version}")
        print(f"Engines: {config.engines}")
    except Exception as e:
        print(f"[ERROR] Could not load config: {e}")

def main():
    parser = argparse.ArgumentParser(description="Continuum CLI (ct)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    init_parser = subparsers.add_parser("init", help="Initialize a new Continuum workspace")
    init_parser.add_argument("project_name", nargs="?", default="my-project", help="Name of the project")
    
    subparsers.add_parser("doctor", help="Check workspace health")
    subparsers.add_parser("validate", help="Validate workspace configuration")
    subparsers.add_parser("version", help="Print Continuum version")
    subparsers.add_parser("config", help="Print current configuration")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_workspace(args.project_name)
    elif args.command == "doctor":
        doctor()
    elif args.command == "validate":
        validate()
    elif args.command == "version":
        print(f"Continuum CLI v{VERSION}")
    elif args.command == "config":
        print_config()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
