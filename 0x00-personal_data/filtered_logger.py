#!/usr/bin/env python3
"""
Personal data
"""
import re


"""
fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;
password=eggcellent;date_of_birth=12/12/1986;",
"name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]
"""
"""
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
"""
"""
function called filter_datum that returns the log message obfuscated:
Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by
which character is separating all fields in the log line (message)
The function should use a regex
to replace occurrences of certain field values.
filter_datum
should be less than 5 lines long and use
re.sub to perform the substitution with a single regex.
"""


def filter_datum(fields: list[str, list], redaction: str,
                 message: str, separator: str) -> str:
    """
    function that returns the log message obfuscated:
    """
    pattern = '|'.join(fields)
    obfuscated = re.sub(pattern + r'=([^{}]+)'.format(separator),
                        r'\1={}{}'.format(redaction, separator), message)

    return obfuscated
