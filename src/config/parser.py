import os
import yaml

class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass

class ContinuumConfig:
    def __init__(self, project_name, version, engines):
        self.project_name = project_name
        self.version = version
        self.engines = engines

    def __repr__(self):
        return f"<ContinuumConfig project={self.project_name} version={self.version}>"

def load_config(workspace_dir="."):
    """
    Loads and parses the continuum.yaml file from a given workspace directory.
    """
    config_path = os.path.join(workspace_dir, "continuum.yaml")
    
    if not os.path.exists(config_path):
        raise ConfigError(f"Configuration file not found: {config_path}. Are you in a Continuum workspace?")

    try:
        with open(config_path, "r") as f:
            raw_config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ConfigError(f"Failed to parse continuum.yaml: {e}")

    if not isinstance(raw_config, dict):
        raise ConfigError("Invalid continuum.yaml format: expected a dictionary.")

    # Validate required fields
    project_name = raw_config.get("project")
    if not project_name:
        raise ConfigError("Missing required field 'project' in continuum.yaml")

    version = raw_config.get("continuum_version", raw_config.get("version", "unknown"))
    
    engines = raw_config.get("engines", {})
    if not isinstance(engines, dict):
        raise ConfigError("Field 'engines' must be a dictionary in continuum.yaml")

    return ContinuumConfig(
        project_name=project_name,
        version=version,
        engines=engines
    )

if __name__ == "__main__":
    # Test script functionality if run directly
    try:
        # Assuming run from a valid workspace
        config = load_config()
        print(f"Successfully loaded configuration for '{config.project_name}' (v{config.version})")
        print(f"Engines: {config.engines}")
    except ConfigError as e:
        print(f"Error: {e}")
