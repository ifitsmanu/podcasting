import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file and returns it as a string.
    """
    reader = PdfReader(pdf_path)
    all_text = []
    for page in reader.pages:
        text = page.extract_text() or ""
        # Clean text if needed
        text = re.sub(r"\s+", " ", text)
        all_text.append(text.strip())
    return "\n".join(all_text)
