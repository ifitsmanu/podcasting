import argparse
import os
import sys
import logging
from utils.audio_processing import merge_audio_segments

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def merge_audio_files(audio_dir: str, output_file: str) -> str:
    merge_audio_segments(audio_dir, output_file)
    return f"Merged audio saved to {output_file}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge audio segments into a single podcast file.")
    parser.add_argument("audio_dir", type=str, help="Directory containing audio segments.")
    parser.add_argument("output_file", type=str, help="Output merged audio file (e.g., final_podcast.mp3).")
    args = parser.parse_args()

    if not os.path.exists(args.audio_dir):
        logging.error(f"Audio directory not found: {args.audio_dir}")
        sys.exit(1)

    try:
        message = merge_audio_files(args.audio_dir, args.output_file)
        logging.info(message)
    except Exception as e:
        logging.error(f"Failed to merge audio: {e}")
        sys.exit(1)
