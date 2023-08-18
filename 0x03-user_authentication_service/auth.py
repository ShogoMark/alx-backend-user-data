#!/usr/bin/env python3
"""hashed passwords"""

import bcrypt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers a new user with email & password"""
        user_exist = self._db.find_user_by(email=email)
        if user_exist:
            raise ValueError(f"User {email} already exists")

        # Hash the password
        hashed_password = self._hash_password(password)

        # create and add the new user to the db
        new_user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
        return new_user



    def _hash_password(self, password: str) -> str:
        """function returns salted hash of input password"""
        salt = bcrypt.gensalt()

        salted_hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        return salted_hashed_password
