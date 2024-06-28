#!/usr/bin/python3
"""
Module for file operations.
"""


def write_file(filename="", text=""):
    """
    Writes text to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
