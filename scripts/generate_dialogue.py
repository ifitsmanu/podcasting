import argparse
import os
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a full dialogue from the plan.")
    parser.add_argument("plan_file", type=str, help="Path to the plan file.")
    parser.add_argument("output_script", type=str, help="Where to save the dialogue script.")
    args = parser.parse_args()

    llm = get_llm()
    plan = open(args.plan_file, "r", encoding="utf-8").read()

    dialogue_template = load_prompt("prompts/two_person_interview_templates.py/dialogue_prompt.txt")
    dialogue_prompt = ChatPromptTemplate.from_template(dialogue_template)

    formatted_input = dialogue_prompt.format(plan=plan)
    response = llm(formatted_input)
    script = response.content.strip()

    with open(args.output_script, "w", encoding="utf-8") as f:
        f.write(script)
    print(f"Dialogue script generated and saved to {args.output_script}")
