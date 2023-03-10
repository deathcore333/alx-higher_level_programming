#!/usr/bin/python3
"""Defines Rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using rectangle."""
    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """String representation of a square"""
        str_rep = "[Square] " + str(self.__size) + "/" + str(self.__height)
        return str_rep
