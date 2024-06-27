#!/usr/bin/python3
"""
Module: file_reader

Provides a function read_file(filename) to read a
text file and print its contents to stdout.
"""


def read_file(filename=""):
    """Reads and prints the contents of a text file."""
    with open(filename, 'r', encoding='UTF8') as file:
        print(file.read())
