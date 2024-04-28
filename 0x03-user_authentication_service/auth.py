#!/usr/bin/env python3
"""
Main file
"""


from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound  # Add this import


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

    def register_user(self, email: str, password: str) -> User:
        """
         take mandatory email and password string arguments
         and
         return a User object.
         If a user already exist with the passed email,
         raise a ValueError with the message
            User <user's email> already exists.
         If not, hash the password with _hash_password,
         save the user to the database
         using self._db and return the User object.
        """
        reg_user = User(email=email)
        try:
            exsisting_user = self._db.find_user_by(email=email)
            if exsisting_user:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            pass
        hashed_password = _hash_password(password)
        reg_user.hashed_password = hashed_password
        self._db.add_user(email, hashed_password)
        return reg_user
