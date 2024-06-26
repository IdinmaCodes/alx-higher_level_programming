#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

The Square class includes methods for initializing the square
with a given size and calculating its area.
"""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
