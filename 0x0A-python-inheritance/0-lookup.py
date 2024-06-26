#!/usr/bin/python3
"""Provides utilities for object introspection."""


def lookup(obj):
    """Returns a list of attributes and methods of the given object."""
    attributes_and_methods = dir(obj)
    return attributes_and_methods
