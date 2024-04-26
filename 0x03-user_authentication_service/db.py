#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from user import Base
from user import User
from typing import TypeVar


key_args = ['id', 'email', 'hashed_password',
            'session_id', 'reset_token']


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        add_user method,
        which has two required string arguments:
        email and hashed_passwor
        and
        returns a User object.
        The method should save the user to the database.
        No validations are required at this stage.
        """
        if not email or not hashed_password:
            return
        Session = self._session
        user = User(email=email, hashed_password=hashed_password)
        Session.add(user)
        Session.commit()
        # Session.close()
        return user

    def find_user_by(self, **keyword) -> User:
        """
        This method takes in arbitrary keyword arguments
        and
        returns the first row found in the users table as filtered
        by the method’s input arguments.
        ensure that SQLAlchemy’s NoResultFound and InvalidRequestError
        are raised when no results are found,
        or when wrong query arguments are passed, respectively.
        Warning:
        NoResultFound has been moved from sqlalchemy.orm.exc to sqlalchemy.exc
        between the version 1.3.x and 1.4.x of SQLAchemy
        - please make sure you are importing it from sqlalchemy.orm.exc
        """
        for key in keyword:
            if key not in key_args:
                raise InvalidRequestError
        Session = self._session
        try:
            return Session.query(User).filter_by(**keyword).one()
        except Exception:
            raise NoResultFound

    def update_user(self, user_id: int, **keyword) -> None:
        """
        DB.update_user method that takes as argument
        a required user_id integer and arbitrary keyword arguments,
        and
        returns None.

        The method will use find_user_by to locate the user to update,
        then will update the user’s attributes as passed in the method’s
        arguments then commit changes to the database.

        If an argument that does not correspond to a user attribute is passed,
        raise a ValueError.
        """
        try:
            user = self.find_user_by(id=user_id)
        except Exception:
            raise ValueError("User not found")
        for key, value in keyword.items():
            if hasattr(User, key):
                setattr(User, key, value)
            else:
                raise ValueError(f"Invalid attribute: {key}")
        self._session.commit()
