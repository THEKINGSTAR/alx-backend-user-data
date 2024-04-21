#!/usr/bin/env python3
"""
Create the class Auth:
in the file api/v1/auth/auth.py
"""


from flask import request
from typing import TypeVar, List
User = TypeVar('User')
from api.v1.auth.auth import Auth



class SessionAuth(Auth):
    """
    SessionAuth that inherits from Auth
    """
    