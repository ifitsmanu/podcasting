import yaml
import os

def load_config(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config
