from langchain.agents import tool
from utils.audio_processing import text_to_speech_line_by_line, merge_audio_segments
from utils.file_manager import ensure_dir
import os

@tool("generate_audio_segments")
def generate_audio_segments_tool(script_text: str, output_dir: str) -> str:
    """Generate audio segments from script text."""
    ensure_dir(output_dir)
    text_to_speech_line_by_line(script_text, output_dir)
    return f"Audio segments generated in {output_dir}"

@tool("merge_audio")
def merge_audio_tool(audio_dir: str, output_file: str) -> str:
    """Merge all audio segments into a single file."""
    merge_audio_segments(audio_dir, output_file)
    return f"Merged audio saved to {output_file}"
