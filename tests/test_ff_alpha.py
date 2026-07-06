import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from engine.runtime import Runtime

def run():
    print("--- Executing Phase 5 (Frontend Force Alpha) ---")
    runtime = Runtime(".")
    runtime.load_org("FrontendForce", "v1")
    runtime.execute_protocol("FrontendForce", "v1", "LandingPage")
    print("--- Done! ---")

if __name__ == '__main__':
    run()
