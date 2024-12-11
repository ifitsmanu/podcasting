import argparse
import os
import sys
from utils.file_manager import ensure_dir
from utils.text_processing import extract_text_from_pdf
import logging

# Set up a basic logger; in a larger system, use a logging config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_pdf_and_save(pdf_path: str, output_path: str):
    """
    Extracts text from the given PDF and saves it to output_path.
    Raises exceptions if something goes wrong.
    """
    ensure_dir(os.path.dirname(output_path))
    extracted_text = extract_text_from_pdf(pdf_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)
    logging.info(f"Text extracted to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file.")
    parser.add_argument("output_path", type=str, help="Path to save the extracted text.")
    args = parser.parse_args()
    
    try:
        parse_pdf_and_save(args.pdf_path, args.output_path)
    except Exception as e:
        logging.error(f"Failed to extract text: {e}")
        sys.exit(1)
