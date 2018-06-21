"""Converts FileMaker key-value pairs to and from python dictionaries."""

import re


escape_dict = {"=": "/=", ":": "/:", ">": "/>", "<": "/<"}


def fm_dict(dict):
    """Convert a python dictionary into an FM dictionary."""
    hashed_str = ''
    for key, value in dict.items():
        hashed_str += hash(key, value)
    return hashed_str


def py_dict(dict):
    """Convert an FM dictionary into a python dictionary."""
    pattern = '<:(.*?):=(.*?):>'
    pairs_list = re.findall(pattern, dict)
    if not pairs_list:
        return dict
    d = {}
    for i in pairs_list:
        key = py_dict(unescape(i[0]))
        value = py_dict(unescape(i[1]))
        d[key] = value
    return d


def hash(key='', value=''):
    """Basic conversion from key-value pair into FM dictionary."""
    key = escape(str(key))
    value = escape(str(value))
    return '<:{}:={}:>'.format(key, value)


def escape(str):
    """Support function. Ensure a string is properly escaped."""
    for i, j in escape_dict.items():
        str = str.replace(i, j)
    return str


def unescape(str):
    """Support function. Ensure a string is properly UNescaped."""
    for i, j in escape_dict.items():
        str = str.replace(j, i)
    return str
