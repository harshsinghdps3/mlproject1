# logger.py
import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Define logs directory and create it if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Define log file path with timestamp
LOG_FILE_PATH = os.path.join(logs_dir, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

# Get or create a logger and set its level
logger = logging.getLogger("AppLogger")
logger.setLevel(logging.INFO)

# Create and configure a rotating file handler
handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=5*1024*1024, backupCount=3)
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Add the handler to the logger (avoiding duplicates if reloaded)
if not logger.handlers:
    logger.addHandler(handler)


if __name__ == "__main__":
    logger.info("Logging has started")
    