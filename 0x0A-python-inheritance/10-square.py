#!/usr/bin/python3
"""Defines a class square inheriting Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size ** self.__size)
