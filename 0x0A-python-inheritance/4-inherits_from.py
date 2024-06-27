#!/usr/bin/python3

"""
Checks inheritance relationships.
"""


def inherits_from(obj, a_class):
    """Returns True if obj's class inherits from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
