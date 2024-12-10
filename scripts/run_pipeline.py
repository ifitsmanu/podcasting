import argparse
import os
import subprocess
import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the entire pipeline from PDF to final audio podcast.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF of the research paper.")
    parser.add_argument("--work_dir", type=str, default="work_output", help="Directory for intermediate outputs.")
    parser.add_argument("--final_audio", type=str, default="final_podcast.mp3", help="Name of the final audio file.")
    args = parser.parse_args()

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    os.makedirs(args.work_dir, exist_ok=True)
    
    # 1. Parse PDF
    text_path = os.path.join(args.work_dir, f"extracted_{timestamp}.txt")
    subprocess.run(["python", "scripts/parse_pdf.py", args.pdf_path, text_path])

    # 2. Generate Plan
    plan_path = os.path.join(args.work_dir, f"plan_{timestamp}.txt")
    subprocess.run(["python", "scripts/generate_plan.py", text_path, plan_path])

    # 3. Generate Dialogue
    draft_script_path = os.path.join(args.work_dir, f"draft_script_{timestamp}.txt")
    subprocess.run(["python", "scripts/generate_dialogue.py", plan_path, draft_script_path])

    # 4. Enhance Script
    enhanced_script_path = os.path.join(args.work_dir, f"enhanced_script_{timestamp}.txt")
    subprocess.run(["python", "scripts/enhance_script.py", draft_script_path, enhanced_script_path])

    # (Optional) Validate Script
    # Example: Uncomment if desired
    # subprocess.run(["python", "scripts/validate_script.py", enhanced_script_path, "--fact_check", "--coherence_check"])

    # 5. Generate Audio Segments
    audio_dir = os.path.join(args.work_dir, f"audio_segments_{timestamp}")
    os.makedirs(audio_dir, exist_ok=True)
    subprocess.run(["python", "scripts/generate_audio.py", enhanced_script_path, audio_dir])

    # 6. Merge Audio
    final_audio_path = os.path.join(args.work_dir, args.final_audio)
    subprocess.run(["python", "scripts/merge_audio.py", audio_dir, final_audio_path])

    print(f"Pipeline complete! Final podcast audio at {final_audio_path}")
