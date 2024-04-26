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



class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
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

    def add_user(self, email: str, hashed_passwor: str) -> User:
        """
        add_user method,
        which has two required string arguments:
        email and hashed_passwor
        and
        returns a User object.
        The method should save the user to the database.
        No validations are required at this stage.
        """
        if not email or not hashed_passwor:
            return
        Session = self._session
        user = User(email=email, hashed_password=hashed_passwor)
        Session.add(user)
        Session.commit()
        # Session.close()
        return user
