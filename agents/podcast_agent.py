from langchain.agents import Tool, ZeroShotAgent, AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from tools.pdf_tools import parse_pdf_tool
from tools.script_tools import generate_plan_tool, generate_dialogue_tool, enhance_script_tool
from tools.validation_tools import fact_check_tool, coherence_check_tool
from tools.audio_tools import generate_audio_segments_tool, merge_audio_tool
from utils.config_loader import load_config
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_podcast_agent():
    # Load pipeline config to decide which steps are used
    pipeline_cfg = load_config("config/pipeline_config.yaml")
    steps = pipeline_cfg["pipeline"]["steps"]
    options = pipeline_cfg["options"]

    # Define tools based on steps
    tools = []
    # Parse PDF
    tools.append(parse_pdf_tool)
    # Generate plan
    tools.append(generate_plan_tool)
    # Generate dialogue
    tools.append(generate_dialogue_tool)
    # Enhance script (if enabled)
    if options.get("use_enhancement", True):
        tools.append(enhance_script_tool)
    # Validate script (if enabled)
    if options.get("use_validation", False):
        tools.append(fact_check_tool)
        tools.append(coherence_check_tool)
    # Generate audio
    tools.append(generate_audio_segments_tool)
    # Merge audio
    tools.append(merge_audio_tool)

    llm = ChatOpenAI(temperature=0.7)

    prefix = """You are a podcast production assistant that uses a set of tools to transform a research paper into a two-person interview-style podcast. The user will provide a PDF path, and you will:
1. Parse PDF
2. Generate a plan
3. Generate a dialogue
4. Enhance script (if option is enabled)
5. Validate script (if option is enabled)
6. Generate audio segments
7. Merge audio into final podcast
You have these tools available:"""

    suffix = "Begin."

    # This agent can be run zero-shot or we can design a more sophisticated approach.
    agent = ZeroShotAgent(llm_chain=None, tools=tools, prefix=prefix, suffix=suffix, input_variables=["input"])
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
    return agent_executor
