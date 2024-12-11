import argparse
import os
import sys
import logging
from utils.file_manager import ensure_dir
from utils.audio_processing import text_to_speech_line_by_line

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_audio_segments(script_text: str, output_dir: str) -> str:
    """
    Generate audio segments from the given script text.
    Saves the resulting mp3 files in output_dir.
    Returns a message indicating success.
    """
    ensure_dir(output_dir)
    text_to_speech_line_by_line(script_text, output_dir)
    return f"Audio segments generated in {output_dir}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate audio segments from the script using ElevenLabs TTS.")
    parser.add_argument("script_file", type=str, help="Path to the enhanced script file.")
    parser.add_argument("output_dir", type=str, help="Directory to save audio segments.")
    args = parser.parse_args()

    if not os.path.exists(args.script_file):
        logging.error(f"Script file not found: {args.script_file}")
        sys.exit(1)

    try:
        with open(args.script_file, "r", encoding="utf-8") as f:
            script = f.read()

        result_message = generate_audio_segments(script, args.output_dir)
        logging.info(result_message)

    except Exception as e:
        logging.error(f"Failed to generate audio segments: {e}")
        sys.exit(1)
