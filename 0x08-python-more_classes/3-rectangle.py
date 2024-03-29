#!/usr/bin/python3
"""This program defines a Rectangle class with its attributes"""


class Rectangle(object):
    """This class defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor function with a private instance attribute
            Args:
                - width(default = 0): int
                - height(default = 0): int
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Getter of the property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of the property height
            Arg:
                - value: int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter of the property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of the property height
            Arg:
                - value: int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"

        return rectangle_str[:-1]
