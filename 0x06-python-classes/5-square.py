#!/usr/bin/python3
"""
A class used to represent a Square

...

Attributes
----------
size : int
    the size of the sides of the square

Methods
-------
area():
    Returns the area of the square.

my_print():
    Prints the square using '#' characters.
"""


class Square:
    def __init__(self, size=0):
        self.size = size

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

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
