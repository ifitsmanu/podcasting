import re
import os
import logging
from PyPDF2 import PdfReader

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file and returns it as a single normalized string.
    Raises FileNotFoundError if the file does not exist.
    Raises ValueError if the PDF cannot be read or is empty.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        raise ValueError(f"Failed to read PDF {pdf_path}: {e}")

    if not reader.pages:
        raise ValueError(f"No pages found in PDF: {pdf_path}")

    all_text = []
    page_count = len(reader.pages)
    logging.info(f"Extracting text from {page_count} pages in {pdf_path}")

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        # Clean text: collapse multiple whitespaces into a single space
        text = re.sub(r"\s+", " ", text)
        text = text.strip()
        logging.debug(f"Extracted text from page {page_num}: {len(text)} characters")
        all_text.append(text)

    combined_text = "\n".join(all_text)
    if not combined_text.strip():
        raise ValueError(f"No readable text found in {pdf_path}")
    
    logging.info(f"Text extraction complete. Total length: {len(combined_text)} characters.")
    return combined_text
