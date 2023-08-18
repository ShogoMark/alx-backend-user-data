#!/usr/bin/env python3
"""hashed passwords"""

import bcrypt


def _hash_password(password: str) -> str:
    """function returns salted hash of input password"""
    salt = bcrypt.gensalt()

    salted_hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return salted_hashed_password
