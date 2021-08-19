import logging

class MessageIsNormal(logging.Filter):
    def filter(self, record):
        return record.levelname in ['DEBUG', 'INFO', 'WARNING']


class MessageIsError(logging.Filter):
    def filter(self, record):
        return record.levelname in ['ERROR', 'CRITICAL']
