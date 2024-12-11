from langchain.agents import tool
from utils.text_processing import extract_text_from_pdf
from utils.file_manager import ensure_dir
import os

@tool("parse_pdf")
def parse_pdf_tool(pdf_path: str) -> str:
    """Extract text from the given PDF and return as a string."""
    text = extract_text_from_pdf(pdf_path)
    return text
