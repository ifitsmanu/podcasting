import argparse
import os
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate the script using fact check or coherence check prompts.")
    parser.add_argument("script_file", type=str, help="Path to the script file.")
    parser.add_argument("--fact_check", action="store_true", help="Run factual accuracy check.")
    parser.add_argument("--coherence_check", action="store_true", help="Run coherence check.")
    args = parser.parse_args()

    llm = get_llm()
    script_text = open(args.script_file, "r", encoding="utf-8").read()

    if args.fact_check:
        fact_template = load_prompt("prompts/validations/fact_check_prompt.txt")
        fact_prompt = ChatPromptTemplate.from_template(fact_template)
        response = llm(fact_prompt.format(script=script_text))
        print("Fact Check Results:\n", response.content)

    if args.coherence_check:
        coherence_template = load_prompt("prompts/validations/coherence_check_prompt.txt")
        coherence_prompt = ChatPromptTemplate.from_template(coherence_template)
        response = llm(coherence_prompt.format(script=script_text))
        print("Coherence Check Results:\n", response.content)
