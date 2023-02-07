#!/usr/bin/python3

"""Defines a class Rectangle"""


class Rectangle:
    """represents an empty class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the class with objects
        Args:
            width (int): represents the width
            height (int): represents the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """"Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns the printable representation
        of the rectangle
        Represents the rectangle using a # char
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns the string representation of the Rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
