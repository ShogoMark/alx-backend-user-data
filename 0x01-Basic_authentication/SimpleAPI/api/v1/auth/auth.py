#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check if authentication is required for given path"""
        return False


    def authorization_header(self, request=None) -> str:
        "method that returns None"
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """method returns None"""
        return None
