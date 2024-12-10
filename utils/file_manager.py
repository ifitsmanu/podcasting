import os

def ensure_dir(dir_path: str):
    """
    Ensures that the directory exists. Creates it if it does not.
    """
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

def save_text_to_file(text: str, file_path: str):
    ensure_dir(os.path.dirname(file_path))
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
