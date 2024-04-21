#!/usr/bin/env python3
"""
Create the class SessionAuth:
in the file api/v1/auth/SessionAuth.py
"""


from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth
User = TypeVar('User')


class SessionAuth(Auth):
    """
    SessionAuth that inherits from Auth
    """
