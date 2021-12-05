"""
Module with some authorization utils
"""
from random import choices
from string import digits, ascii_letters


def random_password(length=15) -> str:
    """
    Return random password with given length, generated from ascii letters and digits

    :param int length: password length
    """
    return ''.join(choices(ascii_letters + digits, k=length))
