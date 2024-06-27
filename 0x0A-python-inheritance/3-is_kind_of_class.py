#!/usr/bin/python3

"""
Checks if an object is an instance of a specific class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
