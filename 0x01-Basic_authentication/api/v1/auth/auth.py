#!/usr/bin/env python3
"""Defines the class Auth"""

from flask import request
from typing import List, TypeVar


class Auth:
    """manages authentication"""

    def require_auth(self, path: str,
                     excluded_paths: List[str],
                     strict_slashes=False) -> bool:
        """check if authentication is required for given path"""
        if not path:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        for paths in excluded_paths:
            paths = paths.rstrip("*")
            if path.find(paths) != -1:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """method that returns None"""
        if request:
            return request.headers.get("Authorization", None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method returns None"""
        return None
