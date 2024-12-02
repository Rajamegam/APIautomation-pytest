import logging
import os
from datetime import datetime


def get_logger():
    logdir = os.path.join(os.getcwd(), "logs")
    log_file = os.path.join(logdir, f"logfile_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    logger = logging.getLogger("API_logger")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        filehandler = logging.FileHandler(log_file)
        error_log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(error_log_format)
        logger.addHandler(filehandler)

    return logger, log_file
