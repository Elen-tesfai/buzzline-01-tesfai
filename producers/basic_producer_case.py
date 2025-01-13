# basic_generator_case.py
# Generate some streaming buzz messages. 

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Define a function to fetch the message interval from the environment
def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some lists for generating buzz messages
ADJECTIVES: list = ["amazing", "funny", "boring", "exciting", "weird"]
ACTIONS: list = ["found", "saw", "tried", "shared", "loved"]
TOPICS: list = ["a movie", "a meme", "an app", "a trick", "a story"]

#####################################
# Define a function to generate buzz messages
#####################################


def generate_messages():
    """
    Generate a stream of buzz messages.
    """
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        yield f"I just {action} {topic}! It was {adjective}."


#####################################
# Define main() function to run this producer.
#####################################


def main() -> None:
    """
    Main entry point for this producer.
    """
    logger.info("START producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Call the function we defined above to get the message interval
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        # Use the time module to pause execution for a specified number of seconds
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    main()