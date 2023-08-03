#!/usr/bin/env python3
import re

def filter_datum(fields, redaction, message, separator):
    regex_pattern = '|'.join(r'(?<=\b{}\=)[^{}]+'.format(re.escape(field), re.escape(separator)) for field in fields)
    return re.sub(regex_pattern, redaction, message)

