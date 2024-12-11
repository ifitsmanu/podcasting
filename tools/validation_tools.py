from langchain.agents import tool
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate

@tool("fact_check_script")
def fact_check_tool(script_text: str) -> str:
    """Run factual accuracy check on script."""
    llm = get_llm()
    fact_template = load_prompt("prompts/validations/fact_check_prompt.txt")
    fact_prompt = ChatPromptTemplate.from_template(fact_template)
    response = llm(fact_prompt.format(script=script_text))
    return response.content.strip()

@tool("coherence_check_script")
def coherence_check_tool(script_text: str) -> str:
    """Run coherence check on script."""
    llm = get_llm()
    coherence_template = load_prompt("prompts/validations/coherence_check_prompt.txt")
    coherence_prompt = ChatPromptTemplate.from_template(coherence_template)
    response = llm(coherence_prompt.format(script=script_text))
    return response.content.strip()
