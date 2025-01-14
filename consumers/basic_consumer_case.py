# consumers/basic_consumer_case.py
# This script consumes the generated log messages and displays them.

import time
from loguru import logger
from utils.utils_logger import get_log_file_path

# Set the path to the log file
LOG_FILE_PATH = get_log_file_path()

def consume_logs():
    """
    This function consumes logs from the log file and prints them.
    It reads the log file line by line.
    """
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            # Here, you can choose how to process the logs.
            print(line.strip())
            time.sleep(1)  # Simulate delay between consuming logs

def main():
    """
    Main function to consume the logs.
    """
    logger.info("START consuming logs...")

    consume_logs()

    logger.info("Finished consuming logs.")

# Only run the `main` function if this script is executed directly
if __name__ == "__main__":
    main()