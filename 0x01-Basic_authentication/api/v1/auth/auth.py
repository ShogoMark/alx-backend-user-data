#!/usr/bin/env python3
"""Defines the class Auth"""

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str,
                     excluded_paths: List[str],
                     strict_slashes=False) -> bool:
        """check if authentication is required for given path"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if path.endswith("/") and excluded_path.endswith("/"):
                if path == excluded_path:
                    return False
            elif path.endswith("/"):
                if path[:-1] == excluded_path:
                    return False
            elif excluded_path.endswith("/"):
                if path == excluded_path[:-1]:
                    return False
            elif path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """method that returns None"""
        if 'Authorization' in request.headers:
            auth_value = request.headers.get('Authorization')
            return f'{auth_value}', 200
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method returns None"""
        return None
