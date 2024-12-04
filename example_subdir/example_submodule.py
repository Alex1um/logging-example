import logging

# We can import created loggers
from logging_init import global_logger

# Or can create local logger
local_logger = logging.getLogger(__name__)


def example_submodule_function():
    global_logger.info("Starting submodule function")
    try:
        raise Exception("Some caught exception")
    except Exception as e:
        local_logger.error(f"Some error was caught: {e}")
