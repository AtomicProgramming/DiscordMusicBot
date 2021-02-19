import logging

LOGGER_FORMAT = "[%(asctime)s][%(levelname)s]: %(message)s"
logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT)
logger = logging.getLogger("MusicBot")
