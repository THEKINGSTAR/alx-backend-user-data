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
import mysql.connector
from os import environ


fields = ["name",
          "email",
          "password",
          "date_of_birth"]
PII_FIELDS = ('name', 'email', 'phone', 'last_login', "user_agent")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """function that returns the log message obfuscated:"""
    for field in fields:
        pattern = rf"{field}=([^{separator}]*)"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """method to filter value in incoming log_records using filter_datum"""
        filterd_msg = filter_datum(self.fields, self.REDACTION,
                                   super().format(record), self.SEPARATOR)
        return filterd_msg


def get_logger() -> logging.Logger:
    """function that returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter())
    logger.addHandler(stream_handler)
    return logger
