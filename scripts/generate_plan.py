import argparse
import os
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a bullet-point podcast plan from a paper.")
    parser.add_argument("paper_txt", type=str, help="Path to the extracted text file of the paper.")
    parser.add_argument("output_plan", type=str, help="Where to save the generated plan.")
    args = parser.parse_args()

    llm = get_llm()  # Returns a ChatOpenAI or similar instance
    paper = open(args.paper_txt, "r", encoding="utf-8").read()

    # Load your plan prompt template
    # Assume you have two_person_interview_templates/plan_prompt.txt
    plan_template = load_prompt("prompts/two_person_interview_templates.py/plan_prompt.txt")
    plan_prompt = ChatPromptTemplate.from_template(plan_template)

    formatted_input = plan_prompt.format(paper=paper)
    response = llm(formatted_input)
    plan = response.content.strip()

    with open(args.output_plan, "w", encoding="utf-8") as f:
        f.write(plan)
    print(f"Plan generated and saved to {args.output_plan}")
