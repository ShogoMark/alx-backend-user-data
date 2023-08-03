#!/usr/bin/env python3
import re
import logging


def filter_datum(fields: str, redaction: str,
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

    def __init__(self, fields: list):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        for field in self.fields:
            record.msg = filter_datum([field], self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)
