import argparse
import os
import sys
from agents.podcast_agent import create_podcast_agent
from utils.file_manager import ensure_dir
from utils.config_loader import load_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the pipeline using Langchain Agent.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF of the research paper.")
    parser.add_argument("--work_dir", type=str, default="work_output", help="Directory for intermediate outputs.")
    parser.add_argument("--final_audio", type=str, default="final_podcast.mp3", help="Name of the final audio file.")
    args = parser.parse_args()

    ensure_dir(args.work_dir)
    # Provide the pipeline agent with instructions and required parameters.
    agent_executor = create_podcast_agent()

    # You can now instruct the agent with a single prompt:
    # Example prompt: "Here is a PDF at: [pdf path], please run the pipeline."
    prompt = f"I have a PDF at '{args.pdf_path}'. Please generate a final podcast. The intermediate outputs should go into '{args.work_dir}' and the final audio file should be named '{args.final_audio}'."
    try:
        result = agent_executor.run(input=prompt)
        print("Pipeline complete!")
        print(result)
    except Exception as e:
        print(f"Error running pipeline: {e}", file=sys.stderr)
        sys.exit(1)
