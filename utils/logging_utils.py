import logging
import logging.config
import os

def setup_logging():
    config_path = "config/logging.conf"
    if os.path.exists(config_path):
        logging.config.fileConfig(config_path)
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Call setup_logging() at the start of your main scripts as needed.
