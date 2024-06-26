#!/usr/bin/python3

"""
Module: square_printer

This module provides a function for printing a
square pattern using the '#' character.

Functions:
- print_square(size): Prints a square of size 'size' using '#' characters.

Exceptions:
- TypeError: Raised if size is not an integer or if it's a float less than 0.
- ValueError: Raised if size is less than 0.
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print('#' * size)
