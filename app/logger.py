from os import mkdir, getcwd, makedirs, getenv
from sys import stdout
import logging
from logging import DEBUG, INFO, WARN, ERROR, FATAL
from logging import basicConfig, debug
from logging import FileHandler, StreamHandler
from os.path import isdir, exists
from datetime import datetime

from app.settings import SETTINGS


def setup():
    if not isdir("logs"):
        mkdir("logs")

    logging_level = 0
    env_logging_level = SETTINGS.LOGGING_LEVEL
    print(env_logging_level)
    if env_logging_level == "DEBUG":
        logging_level = DEBUG
    elif env_logging_level == "INFO":
        logging_level = INFO
    elif env_logging_level in ("WARN", "WARNING"):
        logging_level = WARN
    elif env_logging_level == "ERROR":
        logging_level = ERROR
    elif env_logging_level in ("FATAL", "CRITICAL"):
        logging_level = FATAL

    if not exists(f'{datetime.now().strftime("logs/%m.%Y")}'):
        makedirs(f'{datetime.now().strftime("logs/%m.%Y")}')

    # Setting up logging
    basicConfig(
        level=logging_level,
        format="%(asctime)s - %(levelname)s - [%(module)s] - %(message)s",
        handlers=[
            FileHandler(f'{datetime.now().strftime("logs/%m.%Y/%d.%m.%Y.log")}'),
            StreamHandler(stdout),
        ],
        encoding="utf-32",
    )

    # Ignore "change detected" from uvicorn
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        if "watchfiles.main" in name:
            logging.getLogger(name).propagate = False
        else:
            logging.getLogger(name).propagate = True

    debug(f"Logger set up! Cwd: {getcwd()}")
