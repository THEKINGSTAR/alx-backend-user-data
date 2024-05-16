#!/usr/bin/env python3
"""
MODULE TO FILTER
Personal data
AND HANDLE LOGGING
"""


import re
from typing import List
import re
import logging
from os import environ
import mysql.connector


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """function that returns the log message obfuscated:"""
    for field in fields:
        pattern = rf"{field}=([^{separator}]*)"
        message = re.sub(pattern, f"{field}={redaction};", message)
    return message
