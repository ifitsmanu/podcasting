# Scripts Directory

This folder contains the main scripts that compose the pipeline from a research paper (PDF) to a final two-person podcast audio file.

- **parse_pdf.py**: Extracts text from the PDF and saves it as a `.txt` file.
- **generate_plan.py**: Uses the plan prompt and the extracted text to create a bullet-pointed plan of the podcast.
- **generate_dialogue.py**: Takes the plan and generates a full dialogue script.
- **enhance_script.py**: Refines the script, removing redundancies and improving clarity.
- **generate_audio.py**: Converts each line of the final script into audio segments using ElevenLabs TTS.
- **merge_audio.py**: Merges all audio segments into one cohesive podcast file.
- **validate_script.py** (Optional): Runs fact check or coherence check prompts to ensure quality.
- **run_pipeline.py**: Orchestrates the entire process from PDF to final audio output.

Adjust paths, parameters, and prompts as needed for your environment.
