#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        """Return the current area of the square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            return TypeError("size must be an integer")
        if value < 0:
            return ValueError("size must be >= 0")
        self.__size = value
