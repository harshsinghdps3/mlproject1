import logging
import os
from datetime import datetime

# Create the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Create the logs directory path (without the file name)
logs_path = os.path.join(os.getcwd(), "logs")
# Ensure the logs directory exists
os.makedirs(logs_path, exist_ok=True)
# Create the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")