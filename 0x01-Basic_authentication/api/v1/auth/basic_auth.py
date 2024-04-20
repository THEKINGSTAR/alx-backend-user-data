#!/usr/bin/env python3
"""
Create a class BasicAuth that inherits from Auth.
"""


from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
from models.base import Base


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Return None if authorization_header is None
        Return None if authorization_header is not a string
        Return None if authorization_header
            doesn’t start by Basic (with a space at the end)
        Otherwise, return the value after Basic (after the space)
        You can assume authorization_header contains only one Basic
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Return None if base64_authorization_header is None
        Return None if base64_authorization_header
                    is not a string
        Return None if base64_authorization_header
                    is not a valid Base64 - you can use try/except
        Otherwise, return the decoded value
                    as UTF8 string - you can use decode('utf-8')
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        This method must return 2 values
        Return None, None
                if decoded_base64_authorization_header is None
        Return None, None
                if decoded_base64_authorization_header is not a string
        Return None, None
                if decoded_base64_authorization_header doesn’t contain ':'
        Otherwise,
            return the user email
            and
            the user password - these 2 values must be separated by a :
        You can assume decoded_base64_authorization_header
        will contain only one :
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        else:
            email, password = decoded_base64_authorization_header.split(':', 1)
            return (email, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Return None if user_email is None or not a string
        Return None if user_pwd is None or not a string
        Return None if your database (file)
            doesn’t contain any User instance
            with email equal to user_email -
            you should use the class method search of the User
            to lookup the list of users based on their email.
            Don’t forget to test all cases:
            “what if there is no user in DB?”, etc.
        Return None if user_pwd is not the password of the User instance found
        - you must use the method is_valid_password of User
        Otherwise, return the User instance
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
        except Exception:
            return

        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        You must use authorization_header
        You must use extract_base64_authorization_header
        You must use decode_base64_authorization_header
        You must use extract_user_credentials
        You must use user_object_from_credentials
        """
        header = self.authorization_header(request)
        base64 = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(base64)
        credintials = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(* credintials)
