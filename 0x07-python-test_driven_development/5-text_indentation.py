#!/usr/bin/python3
"""
Module: text_processing

Provides a function to format text.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after '.', '?', and ':'.

    Args:
    - text (str): Text to be processed.

    Raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    lines = result.split('\n')
    for line in lines:
        print(line.strip())
