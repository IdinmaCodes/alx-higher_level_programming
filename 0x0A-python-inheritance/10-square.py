#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry"""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raises exception: not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer values."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes width and height, validates dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size):
        """Initializes size, validates dimensions."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
