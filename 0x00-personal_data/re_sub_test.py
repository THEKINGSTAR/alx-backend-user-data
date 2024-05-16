#!/usr/bin/env python3
"""
TESTING THE REGULAR EXPRESSION SUBSTITUTION
"""


import re


def re_sub_test():
    """
    function that tests the regular expression substitution
    """
    message = "name=Bob, age=30, password=12345"
    pattern = r'password'
    redaction = 'XXX'
    separator = ','
    obfuscated = re.sub(pattern + r'=([^{}]+)'.format(separator),
                        r'\1={}{}'.format(redaction, separator), message)
    print(obfuscated)

re_sub_test()


def filter_datum(fields: list[str, list], redaction: str,
                 message: str, separator: str) -> str:
    """
    function that returns the log message obfuscated:
    """
    for field in fields:
        obfuscated = re.sub(r'=([^{}]+)'.format(separator),
                            r'\1={}{}'.format(redaction, separator), message)
    return obfuscated

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
            "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))


text = "name=Bob, age=30, password=12345"
new_text = re.sub(r"age=30", "age=38", text)
print(new_text)