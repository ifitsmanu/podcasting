import argparse
import os
from utils.file_manager import ensure_dir
from utils.text_processing import extract_text_from_pdf

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file.")
    parser.add_argument("output_path", type=str, help="Path to save the extracted text.")
    args = parser.parse_args()
    
    ensure_dir(os.path.dirname(args.output_path))
    extracted_text = extract_text_from_pdf(args.pdf_path)
    
    with open(args.output_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)
    print(f"Text extracted to {args.output_path}")
