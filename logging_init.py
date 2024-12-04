import logging
import logging.config
import yaml
import sys


# read config from yaml file
with open('./logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

# use config from yaml file
logging.config.dictConfig(config)

# initialize global logger. Completely optional
global_logger = logging.getLogger("root")


def catch_exception(exc_type, exc_value, exc_traceback):
    global_logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


sys.excepthook = catch_exception
