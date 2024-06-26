#!/usr/bin/python3

"""
Module for appending text to files.
"""


def append_write(filename="", text=""):
    """Append text to a file."""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
