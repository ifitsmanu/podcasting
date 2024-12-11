import os
import logging
import openai
from utils.config_loader import load_config
from langchain.chat_models import ChatOpenAI

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_llm():
    """
    Returns a Langchain ChatOpenAI instance configured with settings from config files.
    """
    creds = load_config("config/credentials.yaml")
    settings = load_config("config/settings.yaml")

    openai_key = os.getenv("OPENAI_API_KEY", creds.get("openai_api_key"))
    if not openai_key:
        raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY or update credentials.yaml.")
    openai.api_key = openai_key

    model_name = settings["model"]["name"]
    temperature = settings["model"]["temperature"]
    max_tokens = settings["model"]["max_tokens"]

    logging.info(f"Initializing LLM with model={model_name}, temperature={temperature}, max_tokens={max_tokens}")

    llm = ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=settings["model"]["top_p"],
        frequency_penalty=settings["model"]["frequency_penalty"],
        presence_penalty=settings["model"]["presence_penalty"]
    )

    return llm
