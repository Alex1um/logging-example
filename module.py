import logging

logger = logging.getLogger(__name__)


def module_function():
    logger.info("Starting module function")
    raise Exception("Some uncaught exception")
