import argparse
import os
import sys
import logging
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_dialogue_from_plan(plan_text: str) -> str:
    dialogue_template = load_prompt("prompts/two_person_interview_templates.py/dialogue_prompt.txt")
    dialogue_prompt = ChatPromptTemplate.from_template(dialogue_template)

    llm = get_llm()
    formatted_input = dialogue_prompt.format(plan=plan_text)

    response = llm(formatted_input)
    return response.content.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a full dialogue from the plan.")
    parser.add_argument("plan_file", type=str, help="Path to the plan file.")
    parser.add_argument("output_script", type=str, help="Where to save the dialogue script.")
    args = parser.parse_args()

    if not os.path.exists(args.plan_file):
        logging.error(f"Plan file not found: {args.plan_file}")
        sys.exit(1)

    try:
        with open(args.plan_file, "r", encoding="utf-8") as f:
            plan = f.read()
        script = generate_dialogue_from_plan(plan)
        with open(args.output_script, "w", encoding="utf-8") as f:
            f.write(script)
        logging.info(f"Dialogue script generated and saved to {args.output_script}")
    except Exception as e:
        logging.error(f"Failed to generate dialogue: {e}")
        sys.exit(1)
