#!/usr/bin/python3
"""
Module for reading files.
"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
    """
    with open(filename, encoding='UTF8') as f:
        print(f.read())
