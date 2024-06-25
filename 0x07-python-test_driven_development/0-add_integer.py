#!/usr/bin/python3
"""A function that adds 2 integers"""


def add_integer(a, b=98):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    Returns:
        int: The sum of `a` and `b`, converted to integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
