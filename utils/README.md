# Utils Directory

This directory contains utility modules that support the main pipeline steps.

- **llm_client.py**: Interfaces with the chosen LLM (e.g., OpenAI) for prompt-response workflows.
- **tts_client.py**: Connects to ElevenLabs TTS to generate audio from text.
- **audio_processing.py**: Functions for merging, normalizing, and assembling audio segments.
- **text_processing.py**: Extracts and cleans text from PDFs or other sources.
- **file_manager.py**: Handles file and directory operations.
- **config_loader.py**: Loads and parses YAML configuration files.
- **prompt_loader.py**: Loads prompt templates from text files.
- **logging_utils.py**: Sets up the project’s logging based on `logging.conf`.

Adjust paths, API keys, and logic as needed to fit your project’s specifics.
