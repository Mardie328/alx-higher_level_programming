#!/usr/bin/python3
"""This program create a Rectangle Class"""


class Rectangle(object):
    """This class represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor function with a private instance attribute"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Return the height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Return the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

