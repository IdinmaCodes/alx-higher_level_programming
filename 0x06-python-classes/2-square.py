#!/usr/bin/python3
"""
This module defines a Square class.
The Square class represents a square with size validation.
"""


class Square:
    """
    Square class represents a square object.

    Attributes:
        __size (int): Size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance
        with a given size (default is 0).
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
