import logging
import logging.config
import os

def setup_logging():
    """
    Set up logging using 'config/logging.conf' if available.
    Otherwise, fallback to basic logging configuration.
    
    This function should be called at the start of main scripts
    to ensure consistent logging behavior across the pipeline.
    """
    config_path = "config/logging.conf"
    if os.path.exists(config_path):
        logging.config.fileConfig(config_path)
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.debug("Logging setup complete.")
