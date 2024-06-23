#!/usr/bin/python3
"""
Module for the Square class.

This module defines a class `Square` that represents a square and allows
for the manipulation and calculation of its properties.

Classes:
    Square

Attributes:
    None
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
