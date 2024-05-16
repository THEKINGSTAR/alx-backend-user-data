#!/usr/bin/env python3
"""

"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    a function that expects one string argument name password
    and
    returns a salted, hashed password,
    which is a byte string.

    Use the bcrypt package to perform the hashing (with hashpw).
    """
    pass_encode = password.encode()
    hash_password = bcrypt.hashpw(pass_encode, bcrypt.gensalt())

    return hash_password
