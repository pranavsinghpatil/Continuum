import argparse
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from engine.runtime import Runtime

def main():
    parser = argparse.ArgumentParser(description="Continuum OS Command Line Interface")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_init = subparsers.add_parser("init", help="Initialize a new Continuum workspace")
    parser_init.add_argument("name", nargs="?", default="demo", help="Name of the workspace")

    parser_run = subparsers.add_parser("run", help="Run a protocol from an organization")
    parser_run.add_argument("org", help="Organization name (e.g. frontend-force or continuum-force)")
    parser_run.add_argument("protocol", help="Protocol to run (e.g. LandingPage or GitHubIssue)")

    args = parser.parse_args()

    if args.command == "init":
        print(f"Initializing Continuum workspace: {args.name}")
        print("Done.")
    elif args.command == "run":
        print(f"Booting Continuum Runtime for '{args.org}'...")
        runtime = Runtime(".")
        
        def on_task_created(event):
            task_id = event.payload["task_id"]
            print(f"    [Antigravity Provider] Auto-queued subagent for task: {task_id}")
            
        runtime.bus.subscribe("TaskCreated", on_task_created)
        
        try:
            runtime.load_org(args.org, "v1")
            runtime.execute_protocol(args.org, "v1", args.protocol)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
