# -*- coding: utf-8 -*-

"""
Test retrieving the credentials.
"""

import os.path

import pytest

from coursera import credentials


def test_get_credentials_with_username_and_password_given():
    username, password = credentials.get_credentials(username='user',
                                                     password='pass')
    assert username == 'user'
    assert password == 'pass'


def test_get_credentials_with_username_given(use_keyring=False):
    import getpass
    _getpass = getpass.getpass
    getpass.getpass = lambda x: 'pass'

    username, password = credentials.get_credentials(username='user',
                                                     use_keyring=use_keyring)
    assert username == 'user'
    assert password == 'pass'

    getpass.getpass = _getpass


def test_get_credentials_without_username_given_raises_exception():
    pytest.raises(
        credentials.CredentialsError,
        credentials.get_credentials)


def test_get_credentials_with_keyring():
    if not credentials.keyring:
        return None
    test_get_credentials_with_username_given(True)

    # Test again, this time without getpass
    username, password = credentials.get_credentials(username='user',
                                                     use_keyring=True)
    assert username == 'user'
    assert password == 'pass'
