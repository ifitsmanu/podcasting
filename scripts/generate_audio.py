import argparse
import os
from utils.file_manager import ensure_dir
from utils.audio_processing import text_to_speech_line_by_line

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate audio segments from the script using ElevenLabs TTS.")
    parser.add_argument("script_file", type=str, help="Path to the enhanced script file.")
    parser.add_argument("output_dir", type=str, help="Directory to save audio segments.")
    args = parser.parse_args()

    ensure_dir(args.output_dir)
    script = open(args.script_file, "r", encoding="utf-8").read()
    
    # This function should:
    # - Parse the script line-by-line
    # - Determine the speaker (Manu or Open AI)
    # - Call ElevenLabs API for each line
    # - Save the resulting .mp3 files to output_dir
    text_to_speech_line_by_line(script, args.output_dir)
    print(f"Audio segments generated in {args.output_dir}")
