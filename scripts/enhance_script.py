import argparse
import os
import sys
import logging
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enhance_script_content(draft_script_text: str) -> str:
    enhance_template = load_prompt("prompts/two_person_interview_templates.py/enhance_prompt.txt")
    enhance_prompt = ChatPromptTemplate.from_template(enhance_template)

    llm = get_llm()
    formatted_input = enhance_prompt.format(draft_script=draft_script_text)

    response = llm(formatted_input)
    enhanced_script = response.content.strip()
    return enhanced_script

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhance the script by improving clarity and flow.")
    parser.add_argument("draft_script", type=str, help="Path to the draft script file.")
    parser.add_argument("output_script", type=str, help="Where to save the enhanced script.")
    args = parser.parse_args()

    if not os.path.exists(args.draft_script):
        logging.error(f"Draft script file not found: {args.draft_script}")
        sys.exit(1)

    try:
        with open(args.draft_script, "r", encoding="utf-8") as f:
            draft = f.read()

        enhanced_script = enhance_script_content(draft)
        
        with open(args.output_script, "w", encoding="utf-8") as f:
            f.write(enhanced_script)
        logging.info(f"Enhanced script saved to {args.output_script}")

    except Exception as e:
        logging.error(f"Failed to enhance script: {e}")
        sys.exit(1)
