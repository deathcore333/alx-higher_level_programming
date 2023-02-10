#!/usr/bin/python3
"""Defines a class rectangle that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry"""
    def __init__(self, width, height)
    """Initialize a new Rectangle
    Args:
        width (int): width of the rectangle
        height (int): height of the new Rectangle
    """
    self.integer_validator("width", width)
    self.__width = width
    self.integer_validator("height", height)
    self.__height = heighti

    def area(self):
        """computes the area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
