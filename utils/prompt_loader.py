import os
import logging
from langchain.prompts import PromptTemplate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_prompt(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        prompt_content = f.read()
    logging.info(f"Prompt loaded from {file_path}")
    return prompt_content

def load_prompt_template(file_path: str, input_variables: list) -> PromptTemplate:
    """
    Load a prompt from a file and return a Langchain PromptTemplate.
    input_variables is a list of variables expected in the prompt template.
    """
    prompt_str = load_prompt(file_path)
    return PromptTemplate(template=prompt_str, input_variables=input_variables)
