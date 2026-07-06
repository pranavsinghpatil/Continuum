import os
import sys
import yaml
import argparse

def init_workspace(project_name):
    print(f"Initializing Continuum workspace in '{project_name}'...")
    base_dir = os.path.join(os.getcwd(), project_name)
    
    # Directory structure defined in Milestone 0.1
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
            
        # Create continuum.yaml
        config_path = os.path.join(base_dir, "continuum.yaml")
        config = {
            "project": project_name,
            "continuum_version": "0.1.0",
            "engines": {
                "reasoning": "default",
                "knowledge": "default",
                "workflow": "default",
                "governance": "default"
            }
        }
        
        with open(config_path, "w") as f:
            yaml.dump(config, f, sort_keys=False)
            
        print("✅ Continuum workspace created successfully.")
    except Exception as e:
        print(f"❌ Error creating workspace: {e}")

def main():
    parser = argparse.ArgumentParser(description="Continuum CLI (ct)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # ct init
    init_parser = subparsers.add_parser("init", help="Initialize a new Continuum workspace")
    init_parser.add_argument("project_name", nargs="?", default="my-project", help="Name of the project (default: my-project)")
    
    # ct add
    add_parser = subparsers.add_parser("add", help="Download an organization into the workspace")
    add_parser.add_argument("org_name", help="Name of the organization (e.g. frontend-force)")
    
    # ct run
    run_parser = subparsers.add_parser("run", help="Run the Continuum runtime")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_workspace(args.project_name)
    elif args.command == "add":
        print(f"Downloading organization '{args.org_name}'... (Not Implemented)")
    elif args.command == "run":
        print("Starting Continuum Event-Driven Runtime... (Not Implemented)")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
