#!/usr/bin/python3
"""
Returns a list of attributes and methods of an object.
"""


def lookup(obj):
    attributes_and_methods = dir(obj)
    return attributes_and_methods
