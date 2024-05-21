#!/usr/bin/env python3
"""
Create the class Auth:
in the file api/v1/auth/auth.py
"""


from flask import request
from typing import TypeVar, List
User = TypeVar('User')


class Auth:
    """
    Auth class
    a class to manage the API authentication.
    """
    def header_key(self, request=None) -> str:
        """
        If request is None, returns None

        If request doesn’t contain the header key Authorization,
        returns None

        Otherwise,
        return the value of the header request Authorization
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        return True
        if the path is not in the list of strings excluded_paths:
        excluded_paths contains string path always ending by a /
        This method must be slash tolerant:
        path=/api/v1/status
        and
        path=/api/v1/status/
        must be returned False
        if excluded_paths contains /api/v1/status/
        """
        if path is None or excluded_paths is None:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths or ('*' in path[:-1]) in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        If request is None, returns None

        If request doesn’t contain the header key Authorization,
        returns None

        Otherwise,
        return the value of the header request Authorization
        """
        if request is None:
            return None
        aut_header = request.headers.get('Authorization')
        if not aut_header:
            return None
        else:
            return aut_header

    def current_user(self, request=None) -> User:
        """
        that return None
        - request will be the Flask request object
        """
        return None
