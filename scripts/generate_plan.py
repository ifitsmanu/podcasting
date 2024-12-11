import argparse
import os
import sys
import logging
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_plan_from_paper(paper_text: str) -> str:
    # Load your plan prompt template
    plan_template = load_prompt("prompts/two_person_interview_templates.py/plan_prompt.txt")
    plan_prompt = ChatPromptTemplate.from_template(plan_template)

    llm = get_llm()  # Returns a ChatOpenAI or similar instance
    formatted_input = plan_prompt.format(paper=paper_text)

    response = llm(formatted_input)
    plan = response.content.strip()
    return plan

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a bullet-point podcast plan from a paper.")
    parser.add_argument("paper_txt", type=str, help="Path to the extracted text file of the paper.")
    parser.add_argument("output_plan", type=str, help="Where to save the generated plan.")
    args = parser.parse_args()

    if not os.path.exists(args.paper_txt):
        logging.error(f"Paper text file not found: {args.paper_txt}")
        sys.exit(1)

    try:
        with open(args.paper_txt, "r", encoding="utf-8") as f:
            paper = f.read()
        plan = generate_plan_from_paper(paper)
        with open(args.output_plan, "w", encoding="utf-8") as f:
            f.write(plan)
        logging.info(f"Plan generated and saved to {args.output_plan}")
    except Exception as e:
        logging.error(f"Failed to generate plan: {e}")
        sys.exit(1)
