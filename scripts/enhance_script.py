import argparse
import os
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhance the script by improving clarity and flow.")
    parser.add_argument("draft_script", type=str, help="Path to the draft script file.")
    parser.add_argument("output_script", type=str, help="Where to save the enhanced script.")
    args = parser.parse_args()

    llm = get_llm()
    draft = open(args.draft_script, "r", encoding="utf-8").read()

    enhance_template = load_prompt("prompts/two_person_interview_templates.py/enhance_prompt.txt")
    enhance_prompt = ChatPromptTemplate.from_template(enhance_template)

    formatted_input = enhance_prompt.format(draft_script=draft)
    response = llm(formatted_input)
    enhanced_script = response.content.strip()

    with open(args.output_script, "w", encoding="utf-8") as f:
        f.write(enhanced_script)
    print(f"Enhanced script saved to {args.output_script}")
