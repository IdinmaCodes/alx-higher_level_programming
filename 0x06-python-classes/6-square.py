#!/usr/bin/python3
"""
Square class: Represents a square with methods for
size manipulation and printing.

Attributes:
    __size (int): Private attribute representing the size of the square.

Methods:
    __init__(self, size=0): Initializes a Square object with a specified size.
    size(self): Getter method to retrieve the size of the square.
    size(self, value): Setter method to set the size of the square,
    with validation.
    area(self): Calculates and returns the area of the square.
    my_print(self): Prints the square using '#' characters.
    Prints an empty line if size is 0.
"""


class Square:
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

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
