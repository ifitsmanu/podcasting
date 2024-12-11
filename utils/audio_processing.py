import os
import re
import glob
import logging
from pydub import AudioSegment

# Assuming text_to_speech is imported from somewhere else or defined above
# from utils.tts_client import text_to_speech  # Example

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def merge_audio_segments(input_dir: str, output_file: str):
    """
    Merges all mp3 files in input_dir into a single file (in order).
    Assumes mp3 files are named in a way that sorting them alphabetically or by timestamp works.
    """
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    mp3_files = glob.glob(os.path.join(input_dir, "*.mp3"))
    if not mp3_files:
        raise FileNotFoundError("No audio files found to merge.")

    mp3_files.sort(key=lambda x: x)

    logging.info(f"Merging {len(mp3_files)} mp3 files from {input_dir} into {output_file}")

    merged = AudioSegment.empty()
    for mp3 in mp3_files:
        audio = AudioSegment.from_mp3(mp3)
        merged += audio
    merged.export(output_file, format="mp3")
    logging.info(f"Merged audio saved to {output_file}")

def normalize_audio(input_file: str, output_file: str, target_dbfs: float = -14.0):
    """
    Normalize the audio to a target dBFS level.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    logging.info(f"Normalizing {input_file} to {target_dbfs} dBFS")
    audio = AudioSegment.from_file(input_file)
    change_in_dBFS = target_dbfs - audio.dBFS
    normalized_audio = audio.apply_gain(change_in_dBFS)
    normalized_audio.export(output_file, format="mp3")
    logging.info(f"Normalized audio saved to {output_file}")

def text_to_speech_line_by_line(script: str, output_dir: str, tts_func=None):
    """
    Parse the script line-by-line, identify the speaker, call TTS, and save segments.
    Expects lines in form: "Manu: Some text" or "Open AI: Some text".

    tts_func is an optional parameter to pass a mock or different TTS function for testing.
    """
    if tts_func is None:
        # Assuming text_to_speech is a known function imported from somewhere else
        from utils.tts_client import text_to_speech
        tts_func = text_to_speech

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    lines = script.strip().split("\n")
    index = 0
    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            logging.debug(f"Skipping empty line {line_num}")
            continue

        if ":" not in line:
            logging.warning(f"No colon found in line {line_num}, skipping: {line}")
            continue

        speaker, text = line.split(":", 1)
        speaker = speaker.strip()
        text = text.strip()

        if not speaker or not text:
            logging.warning(f"Invalid format in line {line_num}, speaker or text missing. Skipping.")
            continue

        segment_file = os.path.join(output_dir, f"segment_{index}_{speaker.replace(' ', '_')}.mp3")
        try:
            logging.info(f"Generating TTS for line {line_num}, speaker: {speaker}")
            tts_func(text, speaker, segment_file)
            index += 1
        except Exception as e:
            logging.error(f"Failed to generate TTS for line {line_num} due to {e}. Skipping line.")
