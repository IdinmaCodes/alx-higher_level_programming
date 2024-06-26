#!/usr/bin/python3
"""Prints first name and last name"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted string stating the first and last name.

    Args:
    - first_name (str): The first name to print.
    - last_name (str, optional): The last name to print. Defaults to "".

    Raises:
    - TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name and last_name must be strings")

    print(f"My name is {first_name} {last_name}")
