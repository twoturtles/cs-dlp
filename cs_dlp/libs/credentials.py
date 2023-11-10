# -*- coding: utf-8 -*-

"""
Manages the credential information (passwords, etc).
"""

import getpass
import logging
import os
import platform


class CredentialsError(BaseException):
    """
    Class to be thrown if the credentials are not found.
    """

    pass


def _getenv_or_empty(s):
    """
    Helper function that converts None gotten from the environment to the
    empty string.
    """
    return os.getenv(s) or ""

