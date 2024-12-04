# Must be imported first, before other packages that use logging
import logging_init

import logging
from example_subdir.example_submodule import example_submodule_function
from module import module_function


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("Starting")
    example_submodule_function()
    module_function()
