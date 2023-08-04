#!/usr/bin/env python3
"""A filtering module using regexing"""
import re
import logging
from typing import List
import sys
import user_data


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """obfuscate specified field with redaction string as separator"""
    regex_pattern = '|'.join(r'(?<=\b{}\=)[^{}]+'.format(re.escape(field),
                                                         re.escape(separator))
                             for field in fields)
    return re.sub(regex_pattern, redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initialize the RedactingFormatter class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats the filtered log message"""
        for field in self.fields:
            record.msg = filter_datum([field], self.REDACTION,
                                      record.msg, self.SEPARATOR)
        return super().format(record)


PII_FIELDS = ('name', 'email', 'phone', 'address', 'credit_card')


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object with desired config."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler(sys.stdout)

    formatter = RedactingFormatter(PII_FIELDS)

    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    logger.propagate = False

    return logger
