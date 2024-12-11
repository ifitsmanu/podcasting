import argparse
import os
import sys
import logging
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_fact_check(script_text: str) -> str:
 fact_template = load_prompt("prompts/validations/fact_check_prompt.txt")
 fact_prompt = ChatPromptTemplate.from_template(fact_template)

 llm = get_llm()
 response = llm(fact_prompt.format(script=script_text))
 return response.content.strip()

def run_coherence_check(script_text: str) -> str:
 coherence_template = load_prompt("prompts/validations/coherence_check_prompt.txt")
 coherence_prompt = ChatPromptTemplate.from_template(coherence_template)

 llm = get_llm()
 response = llm(coherence_prompt.format(script=script_text))
 return response.content.strip()

if __name__ == "__main__":
 parser = argparse.ArgumentParser(description="Validate the script using fact check or coherence check prompts.")
 parser.add_argument("script_file", type=str, help="Path to the script file.")
 parser.add_argument("--fact_check", action="store_true", help="Run factual accuracy check.")
 parser.add_argument("--coherence_check", action="store_true", help="Run coherence check.")
 args = parser.parse_args()

 if not os.path.exists(args.script_file):
     logging.error(f"Script file not found: {args.script_file}")
     sys.exit(1)

 try:
     with open(args.script_file, "r", encoding="utf-8") as f:
         script_text = f.read()
     
     if args.fact_check:
         fact_result = run_fact_check(script_text)
         print("Fact Check Results:\n", fact_result)

     if args.coherence_check:
         coherence_result = run_coherence_check(script_text)
         print("Coherence Check Results:\n", coherence_result)

     if not args.fact_check and not args.coherence_check:
         logging.info("No validation checks selected. Use --fact_check or --coherence_check.")
     
 except Exception as e:
     logging.error(f"Failed to run validation: {e}")
     sys.exit(1)
