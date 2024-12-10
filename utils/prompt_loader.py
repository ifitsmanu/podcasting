import os

def load_prompt(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# If you need a more complex system of inserting variables, consider adding a function
# that formats a template string with given variables.
