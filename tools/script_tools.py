from langchain.agents import tool
from utils.llm_client import get_llm
from utils.prompt_loader import load_prompt_template
from utils.file_manager import save_text_to_file
import os

@tool("generate_plan")
def generate_plan_tool(paper_text: str) -> str:
    """Generate a bullet-pointed plan from the paper text."""
    llm = get_llm()
    # Load the prompt template for plan generation
    prompt = load_prompt_template("prompts/two_person_interview_templates.py/plan_prompt.txt", ["paper"])
    from langchain.chains import LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)
    plan = chain.run(paper=paper_text).strip()
    return plan

@tool("generate_dialogue")
def generate_dialogue_tool(plan_text: str) -> str:
    """Generate a dialogue script from the plan."""
    llm = get_llm()
    prompt = load_prompt_template("prompts/two_person_interview_templates.py/dialogue_prompt.txt", ["plan"])
    from langchain.chains import LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)
    dialogue = chain.run(plan=plan_text).strip()
    return dialogue

@tool("enhance_script")
def enhance_script_tool(draft_script: str) -> str:
    """Enhance the script by improving clarity and flow."""
    llm = get_llm()
    prompt = load_prompt_template("prompts/two_person_interview_templates.py/enhance_prompt.txt", ["draft_script"])
    from langchain.chains import LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)
    enhanced = chain.run(draft_script=draft_script).strip()
    return enhanced
