#!/usr/bin/python3

"""
Checks if an object is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class."""
    return type(obj) == a_class
