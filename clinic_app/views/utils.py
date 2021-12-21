"""
Useful tools for keeping views DRY.
"""
from secrets import choice
from string import ascii_letters, digits

from flask import request
from flask_wtf import FlaskForm


def get_pagination_args(default_per_page: int = 20) -> tuple[int, int]:
    """
    Return pagination GET parameters: page, per_page(as a tuple)

    :param default_per_page: default value for per_page (default page is 1 anyway)
    :return: page, per_page
    """
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=default_per_page, type=int)
    return page, per_page


def parse_filters(kwargs_list: list[dict], form: FlaskForm) -> dict:
    """
    Parse GET parameters(filters for get request), using list of kwargs for dict.get() function.
    Kwargs have to contain at least 'key' key.
    Put retrieved values into dict with corresponding keys,
    and patch form fields(with name == kwargs['key']) with these values.

    :param kwargs_list: list of dicts, each dict is used as kwargs for dict.get()
    :param form: flask-WTForm to patch with filters data
    :return: filters dict
    """
    filters = {}
    for kwargs in kwargs_list:
        arg = request.args.get(**kwargs)
        filters[kwargs['key']] = arg
        field = getattr(form, kwargs['key'])
        field.data = arg
    return filters


def extract_filters(keys, form) -> dict:
    """
    Extract field data from given form(basically serialize) into dict, using given keys.
    :param keys: field names and keys in resulting dict
    :param form: flask-WTForm to extract
    :return: dict of filters
    """
    filters = {}
    for key in keys:
        field = getattr(form, key)
        filters[key] = field.data
    return filters


def random_password(length=15) -> str:
    """
    Return random password with given length, generated from ascii letters and digits

    :param int length: password length
    """
    alphabet = ascii_letters + digits
    return ''.join(choice(alphabet) for _ in range(length))
