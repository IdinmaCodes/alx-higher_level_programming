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
        self.__width = width
        self.__height = height
        self.validate_dimensions()

    def validate_dimensions(self):
        """Validates width and height using integer_validator."""
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
