import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler  # For log rotation

# Create the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Create the logs directory path in the current working directory
logs_path = os.path.join(os.getcwd(), "logs")
# Ensure the logs directory exists
os.makedirs(logs_path, exist_ok=True)
# Create the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create a custom logger (avoid using the root logger)
logger = logging.getLogger("Logger")  # Name your logger
logger.setLevel(logging.INFO)  # Set the logging level

# Create a rotating file handler for log rotation (e.g., 5 MB per file, max 3 backups)
handler = RotatingFileHandler(
    LOG_FILE_PATH, maxBytes=5*1024*1024, backupCount=3  # 5 MB per file, keep 3 backups
)
# Define the log message format
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)  # Attach formatter to handler
logger.addHandler(handler)  # Attach handler to logger

# Optional: Add a console handler to also print logs to the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

if __name__ == "__main__":
    logger.info("Logging has started")  # Use the custom logger