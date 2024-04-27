#!/usr/bin/env python3
"""
Main file
"""


from db import DB
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    method that takes in a password string arguments
    and
    returns bytes.
    The returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """
    Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()
