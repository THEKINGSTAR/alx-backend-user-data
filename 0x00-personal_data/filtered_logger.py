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
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    function that returns
    a connector to the database
    (mysql.connector.connection.MySQLConnection object).

    Use the os module to obtain credentials from the environment

    Use the module mysql-connector-python
    to connect to the MySQL database
    (pip3 install mysql-connector-python)
    """
    user_name = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    DB_NAME = environ.get(" PERSONAL_DATA_DB_NAME", "")

    sqlStrng = mysql.connector.connection.MySQLConnection(user=user_name,
                                                          password=password,
                                                          host=host,
                                                          database=DB_NAME)
    return sqlStrng


def main():
    """
    function will obtain a database connection
    using get_db and retrieve all rows in the users table
    and
    display each row under a filtered format
    Filtered fields: * name * email * phone * ssn * password
    Only your main function should run when the module is executed.
    """
    pass


if __name__ == '__main__':
    main()
