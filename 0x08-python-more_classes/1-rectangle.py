#!/usr/bin/python3
"""This program create a Rectangle Class"""


class Rectangle(object):
    """This class represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor function with a private instance attribute"""
        self._Rectangle__width = width
        self._Rectangle__height = height

    def height(self):
        """Return the height of Rectangle"""
        return self._Rectangle__height

    def height(self, value):
        """Set the height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def width(self):
        """Return the width of Rectangle"""
        return self._Rectangle__width

    def width(self, value):
        """Set the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value