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
