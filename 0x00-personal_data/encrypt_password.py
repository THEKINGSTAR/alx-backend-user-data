#!/usr/bin/env python3
"""
Encrypting passwords Module
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    function that expects 2 arguments and returns a boolean.
    Arguments:
    hashed_password: bytes type
    password: string type
    Use bcrypt to validate that the provided password
    matches the hashed password.
    """
    pass_encode = password.encode()
    if bcrypt.checkpw(pass_encode, hashed_password):
        return True
    return False
