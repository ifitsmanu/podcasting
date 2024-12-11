import os
import logging
import requests
from utils.config_loader import load_config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def text_to_speech(text: str, speaker: str, output_path: str):
    """
    Converts text to speech using ElevenLabs TTS and saves to output_path.
    Assumes you have a voice ID from the voices.yaml and an ELEVENLABS_API_KEY set.
    """
    creds = load_config("config/credentials.yaml")
    voices_cfg = load_config("config/voices.yaml")

    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY", creds.get("elevenlabs_api_key"))
    if not elevenlabs_key:
        raise ValueError("ElevenLabs API key not found. Set ELEVENLABS_API_KEY or update credentials.yaml.")

    if speaker.lower() == "manu":
        voice_id = voices_cfg["host"]["voice_id"]
    else:
        voice_id = voices_cfg["guest"]["voice_id"]

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": elevenlabs_key,
        "Content-Type": "application/json"
    }

    stability = voices_cfg.get("stability", 0.5)
    similarity_boost = voices_cfg.get("similarity_boost", 1.0)

    payload = {
        "text": text,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity_boost
        }
    }

    logging.info(f"Calling ElevenLabs TTS: speaker={speaker}, stability={stability}, similarity_boost={similarity_boost}")

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        logging.info(f"TTS audio saved to {output_path}")
    else:
        logging.error(f"ElevenLabs TTS request failed with status {response.status_code}: {response.text}")
        raise Exception(f"ElevenLabs TTS error: {response.status_code}, {response.text}")
