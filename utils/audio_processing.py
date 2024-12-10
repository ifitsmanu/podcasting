from pydub import AudioSegment
import os
import re
import glob

def merge_audio_segments(input_dir: str, output_file: str):
    """
    Merges all mp3 files in input_dir into a single file (in order).
    Assumes mp3 files are named in a way that sorting them alphabetically or by timestamp works.
    """
    mp3_files = glob.glob(os.path.join(input_dir, "*.mp3"))
    if not mp3_files:
        raise Exception("No audio files found to merge.")

    # Sort files by filename or timestamp in filename
    mp3_files.sort(key=lambda x: x)

    merged = AudioSegment.empty()
    for mp3 in mp3_files:
        audio = AudioSegment.from_mp3(mp3)
        merged += audio
    merged.export(output_file, format="mp3")

def normalize_audio(input_file: str, output_file: str, target_dbfs: float = -14.0):
    """
    Normalize the audio to a target dBFS level.
    """
    audio = AudioSegment.from_file(input_file)
    change_in_dBFS = target_dbfs - audio.dBFS
    normalized_audio = audio.apply_gain(change_in_dBFS)
    normalized_audio.export(output_file, format="mp3")

def text_to_speech_line_by_line(script: str, output_dir: str):
    """
    Parse the script line-by-line, identify the speaker, call TTS, and save segments.
    Expects lines in form: "Manu: Some text" or "Open AI: Some text".
    """
    lines = script.strip().split("\n")
    index = 0
    for line in lines:
        if ":" not in line:
            continue
        speaker, text = line.split(":", 1)
        speaker = speaker.strip()
        text = text.strip()

        segment_file = os.path.join(output_dir, f"segment_{index}_{speaker.replace(' ', '_')}.mp3")
        text_to_speech(text, speaker, segment_file)
        index += 1
