#!/usr/bin/env python3
"""
Create the class Auth:
in the file api/v1/auth/auth.py
"""


from flask import request
from typing import TypeVar, List


class Auth:
    """
    Auth class
    a class to manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        that returns False

        -path and excluded_paths
        will be used later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        that returns None
        - request will be the Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        that returns None
        - request will be the Flask request object
        """
        return None
