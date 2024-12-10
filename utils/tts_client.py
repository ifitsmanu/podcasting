import os
import requests
from utils.config_loader import load_config

def text_to_speech(text: str, speaker: str, output_path: str):
    """
    Converts text to speech using ElevenLabs TTS and saves to output_path.
    Assumes you have a voice ID from the voices.yaml and an ELEVENLABS_API_KEY set.
    """
    creds = load_config("config/credentials.yaml")
    voices_cfg = load_config("config/voices.yaml")
    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY", creds.get("elevenlabs_api_key"))

    if speaker.lower() == "manu":
        voice_id = voices_cfg["host"]["voice_id"]
    else:
        voice_id = voices_cfg["guest"]["voice_id"]

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": elevenlabs_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 1.0
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
    else:
        raise Exception(f"ElevenLabs TTS error: {response.status_code}, {response.text}")
