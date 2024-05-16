#!/usr/bin/env python3
"""
Personal data
"""
import re


def filter_datum(fields: list[str, list], redaction: str,
                 message: str, separator: str) -> str:
    """
    function that returns the log message obfuscated:
    """
    pattern = '|'.join(fields)
    obfuscated = re.sub(pattern + r'=([^{}]+)'.format(separator),
                        r'\1={}{}'.format(redaction, separator), message)
    return obfuscated
