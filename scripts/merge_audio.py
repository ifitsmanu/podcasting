import argparse
import os
from utils.audio_processing import merge_audio_segments

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge audio segments into a single podcast file.")
    parser.add_argument("audio_dir", type=str, help="Directory containing audio segments.")
    parser.add_argument("output_file", type=str, help="Output merged audio file (e.g., final_podcast.mp3).")
    args = parser.parse_args()

    merge_audio_segments(args.audio_dir, args.output_file)
    print(f"Merged audio saved to {args.output_file}")
