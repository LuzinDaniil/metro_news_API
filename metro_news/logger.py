import os
import logging
from metro_news.config.const import LOG_FORMAT_DEBUG, DIRECTORY_OF_LOGS
from logging.handlers import RotatingFileHandler


def logger(name):
    """
    Usage:
    from logger import Logger
    logger = Logger(name)
    """
    filename = 'application.log'

    base_logger = logging.getLogger(name)
    base_logger.setLevel(logging.DEBUG)

    formatter_debug = logging.Formatter(LOG_FORMAT_DEBUG, datefmt="%Y-%m-%dT%H:%M:%S%z")

    handler_debug = RotatingFileHandler(os.path.join(DIRECTORY_OF_LOGS, filename), maxBytes=10 ** 8, backupCount=5)
    handler_debug.setLevel(logging.DEBUG)
    handler_debug.setFormatter(formatter_debug)

    base_logger.addHandler(handler_debug)

    return base_logger
