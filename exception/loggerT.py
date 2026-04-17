# loggingT.py

# -------------------------------
# BASIC LOGGING
# -------------------------------

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")


# -------------------------------
# LOGGER, HANDLER, FORMATTER
# -------------------------------

logger = logging.getLogger("my_logger")   # Logger
logger.setLevel(logging.DEBUG)

# handler (console)
console_handler = logging.StreamHandler()

# formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.info("Logger with formatter example")


# -------------------------------
# FILE HANDLER
# -------------------------------

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.error("This goes to file and console")


# -------------------------------
# FILTER (CUSTOM)
# -------------------------------

class OnlyInfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

info_handler = logging.StreamHandler()
info_handler.addFilter(OnlyInfoFilter())

logger.addHandler(info_handler)

logger.info("Only INFO passes filter")
logger.error("This will not pass filter")


# -------------------------------
# ROTATING FILE HANDLER
# -------------------------------

from logging.handlers import RotatingFileHandler

rot_handler = RotatingFileHandler(
    "rotate.log",
    maxBytes=1000,      # file size limit
    backupCount=3       # number of backup files
)

rot_handler.setFormatter(formatter)
logger.addHandler(rot_handler)

logger.warning("Rotating file example")


# -------------------------------
# MULTIPLE HANDLERS
# -------------------------------

# console handler (DEBUG+)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# file handler (ERROR+)
fh = logging.FileHandler("errors.log")
fh.setLevel(logging.ERROR)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("debug message")
logger.error("error message stored in file")


# -------------------------------
# OTHER HANDLERS (REFERENCE)
# -------------------------------

# SMTPHandler → send email
# SysLogHandler → system logs
# MemoryHandler → buffer logs
# HTTPHandler → send logs via HTTP

# Example (just import, not configured)
from logging.handlers import SMTPHandler, SysLogHandler, MemoryHandler, HTTPHandler


# -------------------------------
# CUSTOM CONFIGURATION
# -------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s",
    filename="custom.log",     # log to file
    filemode="w"              # overwrite file
)

logging.info("Custom configured log")


# -------------------------------
# LOGGING LEVEL FILTERING
# -------------------------------

logger.setLevel(logging.WARNING)

logger.debug("ignored")
logger.info("ignored")
logger.warning("shown")
logger.error("shown")