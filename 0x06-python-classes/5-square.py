#!/usr/bin/python3
class Square:
    """
    Square class represents a square object.

    Attributes:
        __size (int): Size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square
        instance with a given size (default is 0).
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square,
        with type and value validation.
        area(self): Computes and returns the area of the square.
        my_print(self): Prints the square with '#' characters.
        If size is 0, prints an empty line.
    """

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
