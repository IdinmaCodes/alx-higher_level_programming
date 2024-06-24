#!/usr/bin/python3

"""
Module for creating Square objects.

The size must be a non-negative integer.

Attributes:
    size (int): The size of the square.

Methods:
    __init__: Initializes the Square object with a given size.

Raises:
    TypeError: If the size is not an integer.
    ValueError: If the size is less than 0.
"""


class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
