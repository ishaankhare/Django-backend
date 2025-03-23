import logging
import sys


class Logger:
    def __init__(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_formatter = logging.Formatter(
            '{{"timestamp":"%(asctime)s.%(msecs)03dZ","app":"de-online-platform-go","level":"%(levelname)s","message":"%(message)s"}}'.format('prod'),
            "%Y-%m-%dT%H:%M:%S"
        )
        stream_handler.setFormatter(stream_formatter)
        stream_handler.setLevel(logging.INFO)
        logger.addHandler(stream_handler)

        self._logger = logger

    def get(self):
        return self._logger


LOGGER = Logger().get()