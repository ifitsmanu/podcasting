import os
import openai
from utils.config_loader import load_config

def get_llm():
    """
    Returns a function or object to interact with the chosen LLM.
    For simplicity, we’ll return a callable that takes a prompt and returns a response.
    """
    creds = load_config("config/credentials.yaml")
    settings = load_config("config/settings.yaml")

    openai.api_key = os.getenv("OPENAI_API_KEY", creds.get("openai_api_key"))
    model_name = settings["model"]["name"]
    temperature = settings["model"]["temperature"]
    max_tokens = settings["model"]["max_tokens"]

    def llm_call(prompt: str):
        completion = openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=settings["model"]["top_p"],
            frequency_penalty=settings["model"]["frequency_penalty"],
            presence_penalty=settings["model"]["presence_penalty"]
        )
        return completion.choices[0].message
    
    return llm_call
